import os
import json
import torch
import pandas as pd
from datasets import Dataset
from transformers import LlamaForCausalLM, LlamaTokenizer, BitsAndBytesConfig, AutoModelForCausalLM

def formatting_prompts_func(example):
    output_texts = []
    for i in range(len(example['question'])):
        text = f"### Question: {example['question'][i]}\n ### Answer: {example['answer'][i]}"
        output_texts.append(text)
    return output_texts

def load_question_answer_data(data_directory, dataset):
    
    script_directory = os.path.dirname(os.path.abspath(__file__))
    data_directory = os.path.join(script_directory, os.pardir, data_directory)
    
    data_path = os.path.join(data_directory, dataset)
    data = open(data_path)
    data_json = json.load(data)

    clean_data = [{'question': entry['input'], 'answer': entry['answer']} for entry in data_json]
    df = pd.DataFrame(clean_data)
    out_data = Dataset.from_pandas(df)
    print('data loaded')
    
    return out_data

def load_model_and_tokenizer(model_dir):
    
    print('loading model')
    model = AutoModelForCausalLM.from_pretrained(
        model_dir,
        # QUANTIZE MODEL, NECESSARY STEP
        quantization_config=BitsAndBytesConfig(
                    load_in_4bit=True,
                    bnb_4bit_compute_dtype=torch.bfloat16,
                    bnb_4bit_use_double_quant=True,
                    bnb_4bit_quant_type='nf4'
                ))

    tokenizer = LlamaTokenizer.from_pretrained(model_dir)
    
    return model, tokenizer
    





