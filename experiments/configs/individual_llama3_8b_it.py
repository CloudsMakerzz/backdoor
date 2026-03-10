import os

os.sys.path.append("..")
from configs.template import get_config as default_config

def get_config():
    
    config = default_config()

    config.tokenizer_paths=["/home/dataset/2024_zox_llm/code/AttnGCG/model/LLM-Research/Llama-3.2-3B"]
    config.model_paths=["/home/dataset/2024_zox_llm/code/AttnGCG/model/LLM-Research/Llama-3.2-3B"]
    config.conversation_templates=['llama-3']
    config.control_init = "a a a a a a a a a a a a a a a a a a a a"
    
    config.attention_weight = 50.0

    return config
