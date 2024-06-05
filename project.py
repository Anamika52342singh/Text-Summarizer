import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format='[%asctime]s:%(message)s:')


project_name='textSummarizer'
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/(project_name)/_init_.py",
    f"src/(project_name)/component_init_.py",
    f"src/(project_name)/utils_init_.py",
    f"src/(project_name)/utils/common_init_.py",
    f"src/(project_name)/logging//_init_.py",
    f"src/(project_name)/config_init_.py",
    f"src/(project_name)/config/configuration_.py",
    f"src/(project_name)/entity_init_.py",
    f"src/(project_name)/constants_init_.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
    "test.py"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:(filedir) for the file {filename}")


    if(not os.path.exists(filepath)) or  (os.path.getsize(filepath)==0)  :
        with open(filepath,'w') as f:
            logging.info(f"creating empty file:{filepath}") 
    else:
        logging.info (f"{filename} is already exists")       
