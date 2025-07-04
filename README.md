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

\[
\text{Overall Score} = \text{Score}_{8B_1} + \text{Score}_{8B_2} + \text{Score}_{26B_1} + \text{Score}_{26B_2}
\]

### For **Score_8B_1** and **Score_8B_2**, follow the steps below:

---

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
huggingface-cli download anonymousdb/LOVE-pretrain temporal.pth ./
huggingface-cli download IntMeGroup/ICCVW_mos0_8B ./IntMeGroup/ICCVW_mos0_8B 
huggingface-cli download IntMeGroup/ICCVW_mos0_st222 ./IntMeGroup/ICCVW_mos0_st222 
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
**make sure the final test images are in dictory GenAIBench/test
**
## 🚀 Evaluation
Run the evaluation script:
```bash
sh shell/eval_score_overall1.sh
sh shell/eval_score_overall2.sh
```
