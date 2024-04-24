# DSAN-5810 Final Project Group 4 - Final Workflow

## Authors

Austin Barish - abb110@georgetown.edu

Landon Carpenter - lc1276@georgetown.edu

Mark Sampson - ms4934@georgetown.edu

Matt Moriarty - mdm341@georgetown.edu

## Repository Naviagation

Here, we give a brief outline of our `final_workflow/` directory to provide for easy navigation.

* `data/`: this directory contains the data used in our final workflow. This includes our training data (both generated and downloaded) and testing data (also both generated and downloaded), as well as `benchmark_output/` and `prod_env/` directories that provide data to us through HELM.

* `eval/`: this directory contains evaluation scripts and results, including `eval.py` and `util_functions.py` for scripting and all `results*` files for compiling pre- and post-fine-tuning results. Furthermore, example results from each of the `results*` text files are compiled in the `results-all.md` file.

* `model_output/`: this directory contains fine-tuned model outputs from our fine-tuning sessions. This includes Llama-2 7B having been fine-tuned on a mathematics dataset (`math_llama/`), then further fine-tuned on a question-and-answer dataset (`math_qa_llama/`). Each of these models contains checkpoints throughout the fine-tuning session to track progress and to store intermediate models in the event of a kernel crash.

* `models/`: similar to `model_output/`, this directory contains models used _before_ fine-tuning. In this case we have the original Llama 7B model (`llama/`), Llama-2 7B (`llama-2-7b/`), Llama-2 7B Chat (`llama-2-7b-chat`), and a HuggingFace-compatible version of Llama-2 7B Chat (`llama-2-7b-chat-hf`).

* `train/`: this directory contains the training scripts used to perform fine-tuning on our models. This includes fine-tuning on mathematics data (`math_training.py`)and question-and-answer data (`qa_training.py`), as well as utility functions to help those processes run more smoothly (`util_functions.py`).