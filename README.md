# AIGVQA

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/IntMeGroup/AIGVQA.git
```

Create and activate a conda environment:

```bash
conda create -n AIGVQA python=3.9 -y
conda activate AIGVQA
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install `flash-attn==2.3.6` (pre-built):

```bash
pip install flash-attn==2.3.6 --no-build-isolation
```

Or compile from source:

```bash
git clone https://github.com/Dao-AILab/flash-attention.git
cd flash-attention
git checkout v2.3.6
python setup.py install
```



# Track I 
Overall Score = Score_8B_1 + Score_8B_2+ Score_26B_1 + Score_26B_2

For Score_8B_1 & Score_8B_2
## 🔧 Preparation
### 📦 Prepare model weights

```bash
cd AIGVQA_8B
export HF_ENDPOINT=https://hf-mirror.com
huggingface-cli download anonymousdb/LOVE-pretrain temporal.pth ./
huggingface-cli download IntMeGroup/ICCVW_mos0_8B ./IntMeGroup/ICCVW_mos0_8B 
huggingface-cli download IntMeGroup/ICCVW_mos0_st222 ./IntMeGroup/ICCVW_mos0_st222 
```
### 📁 Prepare dataset
refine /data/GenAI_mos0.json
"root": your_path_to_GenAIBench

GenAIBench
---val
---train
---test

make sure the final test images are in dictory GenAIBench/test

## 🚀 Evaluation
```bash
sh eval_score_overall1.sh
sh eval_score_overall2.sh
```
