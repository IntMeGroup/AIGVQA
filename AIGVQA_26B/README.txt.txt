cd ICCVW
修改 line13 number=0,1,2,3,4 分别对应 Overall_Traditional Alignment Aesthetic Temporal
Track 1 -- Overall
Track 2 -- Traditional Alignment Aesthetic Temporal
batch 默认 4
batch 调到8 把--eval_steps 改成500

stage1 
sh shell/st1_train.sh

stage2
sh shell/st2_train.sh

