echo [$(date)]: "START"
echo [$(date)]: "creating environment"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activate environment"
source activate ./env
echo [$(date)]: "Create folder and file structure"

for DIR in data_ingestion data_preparation data_validation model model_evaluation model_trainer
do 
    echo "Creating", "src/NER"_$DIR
    mkdir -p "src/NER"_$DIR
    echo "Creating __init__.py inside above folders"
    touch "src/NER"_$DIR/"__init__.py" "src/NER"_$DIR/$DIR.py
    echo "from src.NER_"$DIR.$DIR "import *" >> "src/NER"_$DIR/"__init__.py"
done

echo [$(date)]: "install requirements"
pip install -r requirements.txt -q
echo [$(date)]: "install pytorch depedencies"
pip3 install torch --extra-index-url https://download.pytorch.org/whl/cu113 -q
echo [$(date)]: "END"

# echo [$(date)]: "export conda environment"
# conda env export > conda.yaml
# echo "# ${PWD}" > README.md
# echo [$(date)]: "first commit"
# git add .
# git commit -m "first commit"
# to remove everything -
# rm -rf env/ .gitignore conda.yaml README.md .git/