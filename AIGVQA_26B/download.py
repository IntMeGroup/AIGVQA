import torch
from transformers import AutoTokenizer, AutoModel

# Define the path where you want to store the model
# Make sure this directory exists and you have write permissions
custom_cache_dir = "/fs-computility/ResearchEval/shared/hub/OpenGVLab/"

# --- Important: Ensure the target directory exists ---
# You can create it manually or programmatically:
import os
os.makedirs(custom_cache_dir, exist_ok=True)
# ---------------------------------------------------

model_name = "OpenGVLab/InternVL2_5-26B"

# Download and load the model, specifying the custom cache directory
model = AutoModel.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True,
    use_flash_attn=True,
    trust_remote_code=True,
    cache_dir=custom_cache_dir # <--- This is the key argument
).eval().cuda()

# You can also load the tokenizer similarly
tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    trust_remote_code=True,
    cache_dir=custom_cache_dir # <--- Use the same cache_dir
)

print(f"Model '{model_name}' downloaded and loaded from/to: {custom_cache_dir}")