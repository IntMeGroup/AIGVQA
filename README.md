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
huggingface-cli download IntMeGroup/26B_mos0_20_ep49_6835 --local-dir ./IntMeGroup/26B_mos0_20_ep49_6835
huggingface-cli download IntMeGroup/26B_mos0_100_ep6_6802 --local-dir ./IntMeGroup/26B_mos0_100_ep6_6802
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
## 📊 Output Files and Score process
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
### Average the Overall_MOS in the 4 .csv file to get the final Overall score.
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

### Traditional Score = mos1_Score_8B (8B_mos1_ep200) x0.6 + mos1_Score_26B (26B_mos1_ep2) x0.4
### Alignment Score = mos2_Score_26B_1 (26B_mos2_ep92) x0.5 + mos2_Score_26B_2 (26B_mos2_100_ep16_6458) x0.5
### Aesthetic Score = mos3_Score_8B （ICCVW_mos3_8B）x0.5 + mos3_Score_9B （ICCVW_st2_mos3）x0.5
### Temporal Score = mos4_Score_8B（ICCVW_mos4_8B）x0.4 + mos4_Score_26B_1 (26B_mos4_ep92) x0.2 + mos4_Score_26B_2 (26B_mos4_20_ep33_8076) x0.4

## 1. 🔧 **Preparation AIGVQA_8B**

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
huggingface-cli download IntMeGroup/8B_mos1_ep200 --local-dir ./IntMeGroup/8B_mos1_ep200
huggingface-cli download IntMeGroup/ICCVW_mos3_8B --local-dir ./IntMeGroup/ICCVW_mos3_8B
huggingface-cli download IntMeGroup/ICCVW_mos4_8B --local-dir ./IntMeGroup/ICCVW_mos4_8B
```
### 📁 Prepare dataset
1. Refine the /data/GenAI_mos1.json & /data/GenAI_mos2.json & /data/GenAI_mos3.json & /data/GenAI_mos4.json file with the correct path:
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
sh shell/eval_score_Traditional1.sh
sh shell/eval_score_Aesthetic1.sh
sh shell/eval_score_Temporal1.sh
```

## 2. 🔧 **Preparation AIGVQA_9B**

### 📦 **Prepare Model Weights**

1. Navigate to the `AIGVQA_9B` directory: 

```bash
cd ..
cd AIGVQA_9B
```

2. Set the Hugging Face endpoint:
```bash
export HF_ENDPOINT=https://hf-mirror.com
```

3. Download the required model weights:
```bash
huggingface-cli download anonymousdb/LOVE-pretrain temporal.pth --local-dir ./
huggingface-cli download IntMeGroup/ICCVW_st2_mos3 --local-dir ./IntMeGroup/ICCVW_st2_mos3
```
### 📁 Prepare dataset
1. Refine the  **/data/GenAI_mos3.json** file with the correct path:
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
sh shell/eval_score_Aesthetic2.sh
```

## 3. 🔧 **Preparation AIGVQA_26B**

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
huggingface-cli download IntMeGroup/26B_mos1_ep2 --local-dir ./IntMeGroup/26B_mos1_ep2
huggingface-cli download IntMeGroup/26B_mos2_ep92 --local-dir ./IntMeGroup/26B_mos2_ep92
huggingface-cli download IntMeGroup/26B_mos2_100_ep16_6458 --local-dir ./IntMeGroup/26B_mos2_100_ep16_6458
huggingface-cli download IntMeGroup/26B_mos4_ep92 --local-dir ./IntMeGroup/26B_mos4_ep92
huggingface-cli download IntMeGroup/26B_mos4_20_ep33_8076 --local-dir ./IntMeGroup/26B_mos4_20_ep33_8076
```
### 📁 Prepare dataset
1. Refine the /data/GenAI_mos1.json & /data/GenAI_mos2.json & /data/GenAI_mos3.json & /data/GenAI_mos4.json file with the correct path:
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
sh shell/eval_score_Traditional2.sh
sh shell/eval_score_Alignment1.sh
sh shell/eval_score_Alignment2.sh
sh shell/eval_score_Temporal2.sh
sh shell/eval_score_Temporal3.sh
```
## 📊 Output Files and Score process
After the evaluation you will get 9 score files
```bash
 output_files = [
        'AIGVQA_8B/weights/eval/mos1_1/mos1.csv',
        'AIGVQA_8B/weights/eval/mos3_1/mos3.csv',
        'AIGVQA_8B/weights/eval/mos4_1/mos4.csv',
        'AIGVQA_9B/weights/eval/mos3_2/mos3.csv',
        'AIGVQA_26B/weights/eval/mos1_2/mos1.csv'
        'AIGVQA_26B/weights/eval/mos2_1/mos2.csv'
        'AIGVQA_26B/weights/eval/mos2_2/mos2.csv'
        'AIGVQA_26B/weights/eval/mos4_2/mos4.csv'
        'AIGVQA_26B/weights/eval/mos4_3/mos4.csv'
    ]
```
First delete the "test/" in the video_name colum and then sort the 9 .csv file according to the video_name.
### Calculate the Overall_MOS in the 9 .csv file to get the final 4 scores.
### Traditional Score = AIGVQA_8B/weights/eval/mos1_1/mos1.csv x0.6 + AIGVQA_26B/weights/eval/mos1_2/mos1.csv x0.4
### Alignment Score = AIGVQA_26B/weights/eval/mos2_1/mos2.csv x0.5 + AIGVQA_26B/weights/eval/mos2_2/mos2.csv x0.5
### Aesthetic Score = AIGVQA_9B/weights/eval/mos3_2/mos3.csv x0.5 + AIGVQA_8B/weights/eval/mos3_1/mos3.csv x0.5
### Temporal Score = AIGVQA_8B/weights/eval/mos4_1/mos4.csv x0.4 + AIGVQA_26B/weights/eval/mos4_2/mos4.csv x0.2 + AIGVQA_26B/weights/eval/mos4_3/mos4.csv x0.4
Or you can simply run the python file to process the 9 .csv file
```bash
cd ..
python process_track2.py
```
you will get the prediction.xlsx
