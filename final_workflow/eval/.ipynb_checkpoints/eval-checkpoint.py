from transformers import pipeline
import torch
import json
from util_functions import load_model_and_tokenizer

def evaluate(model_dir, test_data_file, num_samples=10):

    model, tokenizer = load_model_and_tokenizer(model_dir)
    model.eval()

    generation_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        framework='pt', 
    )
    
    print(f'Loading data ...\n')

    with open(test_data_file, 'r') as f:
        test_data = json.load(f)[:num_samples]

    for idx, item in enumerate(test_data, 1):
        
        print(f'========== Iteration {idx} ==========')

        prompt = item['input']
        answer = item['answer']
        output = generation_pipeline(prompt, max_new_tokens=100)

        print(f'PROMPT: {prompt}')
        print(f'OUTPUT: {output}')
        print(f'ANSWER: {answer}\n')

if __name__ == "__main__":
#     model_dir = '../models/llama'
    test_data_file = '../data/test/test_mmlu.json'
#     evaluate(model_dir, test_data_file)
    
    model_dir = '../model_output/math_qa_llama/checkpoint-90'
    evaluate(model_dir, test_data_file)
    
    
