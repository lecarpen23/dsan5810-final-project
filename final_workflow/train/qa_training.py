from trl import SFTTrainer
import torch
import transformers
from util_functions import formatting_prompts_func, load_question_answer_data, load_model_and_tokenizer
from peft import LoraConfig, TaskType
from transformers import TrainingArguments

def train_on_qa(model_dir):
    
    peft_config = LoraConfig(
    r=8,
    task_type="CAUSAL_LM",
    )
    
    model, tokenizer = load_model_and_tokenizer(model_dir)
    
    qa_data = load_question_answer_data('data/train', 'train_qa.json')

    print('sending model to gpu')
    ### NEEDED OR IT WILL BE INCREDIBLY SLOW
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Device is:", device)

    pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.float16,
    )

    
    args = TrainingArguments(
    output_dir='../model_output/math_qa_llama',
    num_train_epochs=6,
    per_device_train_batch_size=32, 
    gradient_accumulation_steps=16,  
    save_steps=10,
    logging_dir='../model_output/logs',
    logging_steps=50,
    save_total_limit=3,
    )

    trainer = SFTTrainer(
        model,
        args=args,
        train_dataset=qa_data,
        formatting_func=formatting_prompts_func,
        max_seq_length = 50, 
        peft_config=peft_config
    )

    print('trainig!')
    trainer.train()

if __name__ == "__main__":
    model_dir = '../model_output/math_llama/checkpoint-1000'
    train_on_qa(model_dir)
