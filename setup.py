from setuptools import find_packages, setup 
from typing import List 

HIPHUN_E_DOT = "-e ."

def get_reqs(file_path:str)-> List[str]:
    '''
    This function return list of requirements.
    Args: File Path
    Returns: List of requirements    
    '''

    reqs = []
    with open(file_path) as file_obj:
        # for line in file_obj:
        #     reqs.append(line.strip())
        reqs = file_obj.readlines() # read line by line and it return line + \n 
        # need to remove \n
        reqs = [r.replace("\n", "") for r in reqs]

        if HIPHUN_E_DOT in reqs:
            reqs.remove(HIPHUN_E_DOT)
    return reqs 


# metadeta info about project
setup(

    name="mlproject",
    version="0.0.1",
    author="jaydeep",
    author_email="jayofficial085@gmail.com",
    packages=find_packages(), # __init__ req 
    install_requires=get_reqs("requirements.txt")


)