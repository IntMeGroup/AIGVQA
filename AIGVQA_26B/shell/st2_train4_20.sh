set -x

GPUS=${GPUS:-1}
BATCH_SIZE=${BATCH_SIZE:-2}
PER_DEVICE_BATCH_SIZE=${PER_DEVICE_BATCH_SIZE:-2}
GRADIENT_ACC=$((BATCH_SIZE / PER_DEVICE_BATCH_SIZE / GPUS))

export CUDA_VISIBLE_DEVICES=1
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
export MASTER_PORT=52224
export TF_CPP_MIN_LOG_LEVEL=3
export LAUNCHER=pytorch
export number=4
OUTPUT_DIR="weights/st2/mos${number}_st2_20"

if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir -p "$OUTPUT_DIR"
fi

torchrun \
  --nnodes=1 \
  --node_rank=0 \
  --master_addr=127.0.0.1 \
  --nproc_per_node=${GPUS} \
  --master_port=${MASTER_PORT} \
  train/stage2_train_AIGV.py \
   --model_name_or_path "/fs-computility/ResearchEval/shared/hub/OpenGVLab/InternVL2_5-26B/ICCVW0622/weights/st1/mos${number}_st1" \
  --conv_style "internlm2-chat" \
  --output_dir ${OUTPUT_DIR} \
  --meta_path "data/GenAI_mos${number}.json"\
  --output_file "${OUTPUT_DIR}/mos${number}_results.csv"\
  --metrics_file "${OUTPUT_DIR}/mos${number}_metrics.txt"\
  --overwrite_output_dir True \
  --force_image_size 448 \
  --max_dynamic_patch 6 \
  --down_sample_ratio 0.5 \
  --drop_path_rate 0.1 \
  --use_llm_lora 16\
  --use_backbone_lora 16\
  --freeze_llm True \
  --freeze_mlp True \
  --freeze_backbone True \
  --vision_select_layer -1 \
  --dataloader_num_workers 4 \
  --bf16 True \
  --num_train_epochs 100 \
  --per_device_train_batch_size ${PER_DEVICE_BATCH_SIZE} \
  --gradient_accumulation_steps ${GRADIENT_ACC} \
  --evaluation_strategy "steps" \
  --save_strategy "steps" \
  --save_steps 4000000 \
  --eval_steps 20\
  --save_total_limit 1 \
  --learning_rate 4e-5 \
  --weight_decay 0.01 \
  --warmup_ratio 0.03 \
  --lr_scheduler_type "cosine" \
  --logging_steps 1 \
  --max_seq_length 4096 \
  --do_train True \
  --grad_checkpoint True \
  --group_by_length True \
  --dynamic_image_size True \
  --use_thumbnail True \
  --ps_version 'v2' \
  --deepspeed "zero_stage1_config.json" \
  --report_to "tensorboard" \
  2>&1 | tee -a "${OUTPUT_DIR}/training_log.txt"
