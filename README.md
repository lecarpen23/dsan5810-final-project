# DSAN-5810 Final Project Group 4

## Authors

Austin Barish - abb110@georgetown.edu

Landon Carpenter - lc1276@georgetown.edu

Mark Sampson - ms4934@georgetown.edu

Matt Moriarty - mdm341@georgetown.edu

## Project Description

The project description is as follows, directly from the DSAN-5810 course website:

> "The task is to fine-tune an open source language model on datasets of your choosing, with the goal of achieving improved performance on a set of NLP benchmark tasks that test a wide range the knowledge and reasoning. We will use the Holistic Framework for Evaluating Foundational Models (<a href="https://crfm.stanford.edu/helm/classic/latest/#/leaderboard">HELM</a>) to facilitate evaluation. You are free to use a combination of finetuning and in-context learning, with some restrictions (outlined below). As such, the selection of the finetuning data is crucial, as is the selection of the pretrained model. This is a unique opportunity to explore diverse data sources and their influence on foundational model behavior."

### Evaluation Datasets

Here, we list the datasets that we aim to evaluate on:

|Dataset  |Function  |Source  |HELM Scenario
|:---:|:---:|:---:|:---:
BigBench | General | https://github.com/google/BIG-bench | https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/big_bench_scenario.py
MMLU | Knowledge | https://github.com/hendrycks/test | https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/mmlu_scenario.py
TruthfulQA (Multiple Choice Single Value) | Knowledge / Harm | https://github.com/sylinrl/TruthfulQA | https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/truthful_qa_scenario.py
CNN/DailyMail | Summarization | https://github.com/deepmind/rc-data | https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/summarization_scenario.py
GSM8k | Math | https://github.com/openai/grade-school-math | https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/gsm_scenario.py
BBQ | Bias | https://github.com/nyu-mll/BBQ | https://github.com/stanford-crfm/helm/blob/main/src/helm/benchmark/scenarios/bbq_scenario.py

### Evaluation Criteria

Final scores will be determined using the geometric mean accross scores obtained on the above benchmarks:

$$
{\displaystyle score = \prod_{i}^{} score(task_i)}
$$


## Repository Naviagation

Here, we give a brief outline of our repository to provide for easy navigation.

* `docs/`: this directory contains the original documents that were provided to us in the repository, such as a `requirements.txt` file for making a virtual environment and an `example.ipynb` Jupyter Notebook that provides a basic example of how to use Python within Jupyter Notebook.

* `final_workflow/`: this directory contains all components of our final workflow. This includes raw models that we downloaded, fine-tuned versions of those models, training and evaluation pipelines, and even the data we used for training, validation, and testing purposes.

* `info/`: this directory contains information-related documents that were helpful in our work on this project. This includes the `LICENSE` that we were given when accessing Large Language Models from HuggingFace, `HELPFUL-COMMANDS{.txt, .md}` files that store the most useful commands that we frequently revisited, and more.

* `sandbox/`: this directory _appears_ empty, but actually contains our virtual environment, `.venv/`. The virtual environment itself is akin to a "sandbox" in that we are constantly playing around in it by adding and removing packages until we have the right configuration to apply to our workflow. With so many packages being utilized, the virtual environment is not directly in the repository, but exists remotely in the file system associated with our GPU.

* `trial-error/`: this directory contains a collection of different files and artifacts that represent the attempts we made throughout the project that were unsuccessful, thus not belonging in the `final_workflow/` directory. This includes evaluation attempts made on HELM, model quantization attempts, fine-tuning attempts, and more.

* `.gitignore`: this file is our gitignore file, telling our repository which files to ignore when making a push. This file tells the repository to ignore large models, large data files, and other directories that may contain a lot of unnecessary files that do not belong in the repository.

* `README.md`: this file is, of course, the README file that describes the repository.

Please note that the `final_workflow/` and `trial-error/` directories have additional `README` files within them to further describe the files within them.

