### FROM https://github.com/meta-llama/llama-recipes/blob/main/recipes/finetuning/finetuning.py

# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

import fire
from llama_recipes.finetuning import main

if __name__ == "__main__":
    fire.Fire(main)