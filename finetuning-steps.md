# How to Finetune

Using llama recipes we can easily fine tune with:

```bash
python -m finetuning.py  --use_peft --peft_method lora --quantization --use_fp16 --model_name /patht_of_model_folder/7B --output_dir Path/to/save/PEFT/model
```

Of note, I had to **downgrade peft to version 0.9 to work correctly**. This seems to have also been noted on the [issues page](https://github.com/huggingface/peft/issues/108) of llama-recipes.

Similarly, I got this error:

```bash
/workspace/anly5810/sandbox/.venv/bin/python: Error while finding module specification for 'finetuning.py' (ModuleNotFoundError: __path__ attribute not found on 'finetuning' while trying to find 'finetuning.py'). Try using 'finetuning' instead of 'finetuning.py' as the module name.
```

But following its instructions, the following command worked:

```bash
python -m finetuning --use_peft --peft_method lora --quantization --use_fp16 --model_name evaluation/local-models/math-llama --output_dir evaluation/local-models/llama-math-output
```

# Finetuning Steps Taken

1. Basic finetuning using llama-recipes
    * `input-model`: math-llama (renamed version of llama-2-7b-chat-hf)
    * `output-model`: llama-math-output
    * `finetuning-data`: [samsum data](https://huggingface.co/datasets/samsum)
        * I did not pass a dataset and this is the default for llama-recipes
    * `Time`: Roughly 2 hours
        
