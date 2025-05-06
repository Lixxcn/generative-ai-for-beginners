```sh
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
conda deactivate
# conda remove -n ai4beg --all

pip install --upgrade pip setuptools wheel
pip install -r requirements.txt


```
