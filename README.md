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



# Track I - Overall Score Calculation

The **Overall Score** is calculated as:

### Overall Score = Score_8B_1x0.25 + Score_8B_2x0.25+ Score_26B_1x0.25 + Score_26B_2x0.25

---

### For **Score_8B_1** and **Score_8B_2**, follow the steps below:

## 🔧 **Preparation**

### 📦 **Prepare Model Weights**

1. Navigate to the `AIGVQA_8B` directory: 

```bash
cd AIGVQA_8B
```

2. Set the Hugging Face endpoint:
```bash
export HF_ENDPOINT=https://hf-mirror.com
```

3. Download the required model weights:
```bash
huggingface-cli download anonymousdb/LOVE-pretrain temporal.pth --local-dir ./
huggingface-cli download IntMeGroup/ICCVW_mos0_8B --local-dir ./IntMeGroup/ICCVW_mos0_8B 
huggingface-cli download IntMeGroup/ICCVW_mos0_st222 --local-dir ./IntMeGroup/ICCVW_mos0_st222 
```

### 📁 Prepare dataset
1. Refine the /data/GenAI_mos0.json file with the correct path:
```bash 
"root": your_path_to_GenAIBench
```

2. Ensure the dataset is structured as follows:
```bash 
GenAIBench
├── val
├── train
└── test
```
### make sure the final test images are in dictory GenAIBench/test

## 🚀 Evaluation
Run the evaluation script:
```bash
sh shell/eval_score_overall1.sh
sh shell/eval_score_overall2.sh
```

### For **Score_26B_1** and **Score_26B_2**, follow the steps below:

## 🔧 **Preparation**

### 📦 **Prepare Model Weights**

1. Navigate to the `AIGVQA_26B` directory: 

```bash
cd ..
cd AIGVQA_26B
```

2. Set the Hugging Face endpoint:
```bash
export HF_ENDPOINT=https://hf-mirror.com
```

3. Download the required model weights:
```bash
huggingface-cli download anonymousdb/LOVE-pretrain temporal.pth --local-dir ./
huggingface-cli download IntMeGroup/ICCVW_mos0_8B --local-dir ./IntMeGroup/26B_mos0_20_ep49_6835
huggingface-cli download IntMeGroup/ICCVW_mos0_st222 --local-dir ./IntMeGroup/26B_mos0_100_ep6_6802
```

### 📁 Prepare dataset
1. Refine the /data/GenAI_mos0.json file with the correct path:
```bash 
"root": your_path_to_GenAIBench
```

2. Ensure the dataset is structured as follows:
```bash 
GenAIBench
├── val
├── train
└── test
```
### make sure the final test images are in dictory GenAIBench/test

## 🚀 Evaluation
Run the evaluation script:
```bash
sh shell/eval_score_overall3.sh
sh shell/eval_score_overall4.sh
```
## 📊 Output File and Score process
After the evaluation you will get 4 score files
```bash
 output_files = [
        'AIGVQA_8B/weights/eval/mos0_1/mos0.csv',
        'AIGVQA_8B/weights/eval/mos0_2/mos0.csv',
        'AIGVQA_26B/weights/eval/mos0_3/mos0.csv',
        'AIGVQA_26B/weights/eval/mos0_4/mos0.csv'
    ]
```
First delete the "test/" in the video_name colum and then sort the 4 .csv file according to the video_name.
# Average the Overall_MOS in the 4 .csv file to get the final Overall score.
Or you can simply run the python file to process the 4 .csv file
```bash
cd ..
python process_overall.py
```
you will get the prediction.xlsx

# Track II - 4 Dimension Score Calculation
Traditional_MOS -- MOS1
Alignment_MOS -- MOS2
Aesthetic_MOS -- MOS3
Temporal_MOS --MOS4

## Traditional_MOS
### Traditional Score = mos1_Score_8Bx0.5 + mos1_Score_26Bx0.5
```bash
huggingface-cli download IntMeGroup/8B_mos1_ep200
huggingface-cli download IntMeGroup/26B_mos1_ep2
```
### Alignment Score = mos2_Score_26B_1x0.5 + mos2_Score_26B_2x0.5
```bash
huggingface-cli download IntMeGroup/26B_mos2_ep92
huggingface-cli download IntMeGroup/26B_mos2_100_ep16_6458
```
### Aesthetic Score = mos3_Score_8Bx0.5 + mos3_Score_9Bx0.5
```bash
huggingface-cli download IntMeGroup/ICCVW_st2_mos3
huggingface-cli download IntMeGroup/ICCVW_mos3_8B
```
### Temporal Score = mos4_Score_8Bx0.4 + mos4_Score_26B_1x0.3 + mos4_Score_26B_2x0.3
```bash
huggingface-cli download IntMeGroup/ICCVW_mos4_8B
huggingface-cli download IntMeGroup/26B_mos4_20_ep33_8076
huggingface-cli download IntMeGroup/26B_mos4_ep92
```
