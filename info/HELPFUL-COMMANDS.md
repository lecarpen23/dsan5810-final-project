
# HELPFUL COMMANDS FOR USE THROUGHOUT THIS PROJECT

----------

## CHANGING GIT USERS

```{bash}
root@jupyterlab-6b4944f65b-jlhx6:/workspace/anly5810# git config --global user.name "My Name"
root@jupyterlab-6b4944f65b-jlhx6:/workspace/anly5810# git config --global user.email "myemail@example.com"
```

* For example,

```{bash}
root@jupyterlab-6b4944f65b-jlhx6:/workspace/anly5810# git config --global user.name "mattmoriarty341"
root@jupyterlab-6b4944f65b-jlhx6:/workspace/anly5810# git config --global user.email "mdm341@georgetown.edu"
```

* Note that you probably will not be able to perform any git commands if you are not the current user. To see who the current user is, use the following command:

```{bash}
root@jupyterlab-6b4944f65b-jlhx6:/workspace/anly5810# git config --list
```

----------

## CREATING VIRTUAL ENVIRONMENT

* Use these if we need these packages

```{bash}
root@jupyterlab-6b4944f65b-jlhx6:/workspace/anly5810# apt-get update
root@jupyterlab-6b4944f65b-jlhx6:/workspace/anly5810# apt-get install python3-venv
```

* Use this to create the virtual environment with the preexisting packages in the original environment (e.g. torch)

```{bash}
root@jupyterlab-6b4944f65b-jlhx6:/workspace/anly5810# python -m venv --system-site-packages .venv
```

----------

## ACTIVATING VIRTUAL ENVIRONMENT

```{bash}
root@jupyterlab-6b4944f65b-jlhx6:/workspace/anly5810# source sandbox/.venv/bin/activate
```

* Note that this will add a "(.venv)" to the beginning of the line in the terminal, indicating that the virtual environment has been activated.

----------

## DEACTIVATING VIRTUAL ENVIRONMENT
```{bash}
(.venv) root@jupyterlab-6b4944f65b-jlhx6:/workspace/anly5810# deactivate
```
* Notice how the "(.venv)" part before the line in the terminal indicates that the virtual environment is activated. After deactivating, this will go away.

----------

## ENABLING VIRTUAL ENVIRONMENT TO BE CHOSEN AS A KERNEL IN JUPYTER NOTEBOOK
```{bash}
(.venv) root@jupyterlab-6b4944f65b-jlhx6:/workspace/anly5810# python -m ipykernel install --user --name=venv --display-name="venv"
python3 -m ipykernel install --user --name=.venv --display-name='venv'
```
----------

## ENABLING HUGGINGFACE USAGE
```{bash}
(.venv) root@jupyterlab-6b4944f65b-jlhx6:/workspace/anly5810# huggingface-cli login
```
----------

## INSTALLING PACKAGES WE NEED

```{bash}
(.venv) root@jupyterlab-6b4944f65b-jlhx6:/workspace/anly5810# pip install transformers
(.venv) root@jupyterlab-6b4944f65b-jlhx6:/workspace/anly5810# pip install accelerate
```

* Notice how the "(.venv)" part before the line in the terminal indicates that the virtual environment is activated. We need it to be activated when we install these packages, otherwise the packages will not be install in the virtual environment.


----------

## DOWNLOADING LLAMA

*With venv activated in the folder you want the model in*

```{bash}
git clone https://github.com/meta-llama/llama.git

cd llama

pip install -e .

chmod -x download.sh

./download.sh

# You will now be prompted to enter your authentication link that you can get by filling out https://ai.meta.com/resources/models-and-libraries/llama-downloads/
# Note: The link is only active for 24 hours
# It will ask what models you want, I did 7B,7B-chat
# The models should now be in llama/llama-2-7b and llama/llama-2-7b-chat
```

----------
## MAKING LLAMA HUGGING FACE COMPATIBLE

**Instructions are here: https://ai.meta.com/blog/5-steps-to-getting-started-with-llama-2/**
**Be sure to already have the models downloaded**

```{bash}
pip install transformers
pip install accelerate

ln ./tokenizer.model ./llama-2-7b-chat/tokenizer.model 

TRANSFORM=`python -c "import transformers;print('/'.join(transformers.__file__.split('/')[:-1])+'/models/llama/convert_llama_weights_to_hf.py')"`
pip install protobuf && python $TRANSFORM --input_dir ./llama-2-7b-chat --model_size 7B --output_dir ./llama-2-7b-chat-hf
```

*You should now have ./llama/llama-2-7b-chat-hf which can be accessed using hugging face transformers package*


------------
## Run an Evaluation

0. Make sure helm is installed (it should be on venv) using:

```{bash}
pip install git+https://github.com/stanford-crfm/helm.git
```

1. Make sure your model is ready for evaluation
2. Edit conf file to point to the model you want to use, each entry should have model=your_model
3. Run evaluations:

```{bash}
helm-run --conf-paths run_specs.conf --suite v1 --max-eval-instances 10 --server-url localhost:5812 --enable-local-huggingface-models <path-to-model>

# the below should be the 'full' neurIPS model evaluation -- which is the same as our project eval
helm-run --conf-paths run_specs.conf --suite v1 --max-eval-instances 10
helm-summarize --suite v1
```

4. View Results

    a. Print Results using:
```{bash}
        helm-summarize --suite v1
```
        
    b. Launch web server
```{bash}
        helm-server --suite v1
```
     


------------
## extra packages that we may or may not need in the venv (should already be in there)

```{bash}
pip install packaging
pip install numpy
pip install pandas
pip install torch torchvision torchaudio
```

------------

helm-run --run-entries "mmlu:subject=anatomy,model_deployment=simple/model1" --suite v1 --max-eval-instances 10

helm-summarize --suite v1

helm-server -p 5812

------------

helm-run --run-entries "mmlu:subject=anatomy,model_deployment=/workspace/anly5810/evaluation/local-models/llama-2-7b-hf" --suite v1 --max-eval-instances 10

helm-summarize --suite v1

helm-server -p 5812

------------

helm-run --run-entries "mmlu:subject=anatomy,model_deployment=meta-llama/Llama-2-7b-chat-hf" --suite v1 --max-eval-instances 10

helm-summarize --suite v1

helm-server -p 5812

-------------

/workspace/anly5810/sandbox/.venv/lib/python3.10/site-packages/helm/config/

--enable-huggingface-models

--base-path option

 helm-run --run-entries "mmlu:subject=anatomy,model_deployment=microsoft/phi-2" --enable-huggingface-models microsoft/phi-2 --base-path --suite v1 --max-eval-instances 10