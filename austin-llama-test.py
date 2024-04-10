# Following: https://ai.meta.com/blog/5-steps-to-getting-started-with-llama-2/

import torch
import transformers
from transformers import LlamaForCausalLM, LlamaTokenizer
import warnings

warnings.filterwarnings("ignore", message="TypedStorage is deprecated.*")

print("Loading model...\n")

# Load Model
model_dir = "./evaluation/local-models/llama-2-7b-chat-hf"
model = LlamaForCausalLM.from_pretrained(model_dir)

# Load Tokenizer
tokenizer = LlamaTokenizer.from_pretrained(model_dir)

# Specify device
### NEEDED OR IT WILL BE INCREDIBLY SLOW
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Device is:", device)

# Create Pipeline
pipeline = transformers.pipeline(
    "text-generation",

    model=model,

    tokenizer=tokenizer,

    torch_dtype=torch.float16,
    
    device=device

)

done = False

while not done:
    # Let user give prompt
    prompt = input("Please enter your input: ")
    prompt = str(prompt) + '\n'

    # Update
    print("Creating Outputs... \n")

    # Create ouptput
    sequences = pipeline(
        prompt,

        do_sample=True,

        top_k=10,

        num_return_sequences=1,

        eos_token_id=tokenizer.eos_token_id,

        max_length=400,

        truncation=True

    )

    # Update
    print("DONE! Here are your outputs:\n")

    # Print Output
    for seq in sequences:

        print(f"{seq['generated_text']}")
        
    keep_going = input("Would you like to enter something else?[Y/N]")
    
    if keep_going.lower() == 'y':
        continue
    else:
        done = True