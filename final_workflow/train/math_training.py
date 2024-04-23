from trl import SFTTrainer
import torch
import transformers
from util_functions import formatting_prompts_func, load_question_answer_data, load_model_and_tokenizer
from peft import LoraConfig, TaskType
from transformers import TrainingArguments
import os

def train_on_math(model_dir):
    
    peft_config = LoraConfig(
    r=8,
    task_type="CAUSAL_LM",
    )
    
    model, tokenizer = load_model_and_tokenizer(model_dir)
    
    math_train_data = load_question_answer_data('data/train', 'eval_math.json')
    math_eval_data = load_question_answer_data('data/test', 'test_math.json')

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Device is:", device)

    pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.float16,
    )
    
    args = TrainingArguments(
    output_dir='../model_output/math_llama',
    num_train_epochs=3,
    per_device_train_batch_size=32, 
    gradient_accumulation_steps=16,  
    save_steps=100,
    logging_dir='../model_output/logs',
    logging_steps=50,
    evaluation_strategy="steps",
    eval_steps=250,
    save_total_limit=3,
    )

    trainer = SFTTrainer(
        model,
        args=args,
        train_dataset=math_train_data,
        eval_dataset = math_eval_data,
        formatting_func=formatting_prompts_func,
        max_seq_length = 50, 
        peft_config=peft_config
    )

    trainer.train()

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    model_dir = '../models/llama'
    train_on_math(model_dir)
