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
## 🔧 Preparation
### 📦 Prepare model weights

```bash
huggingface-cli download anonymousdb/LOVE-pretrain temporal.pth ./
```


# Track I 
Overall Score = S_8B1 + S_8B2+ S26B_1 + S26B_2

For S_8B1 & S_8B2
```bash
cd AIGVQA_8B
sh eval_score_overall1.sh
sh eval_score_overall2.sh
```
