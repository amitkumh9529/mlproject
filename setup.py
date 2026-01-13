from setuptools import find_packages ,setup
from typing import List, Optional

# HYPHEN_E_DOT = "-e ."

def get_requirements() -> List[str]:
    requirements_lst:List[str] = [] 
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirements = line.strip()
                if requirements and requirements != '-e.':
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print('requirements.txt not found') 
    return requirements_lst    

setup(
name='mlproject',
version='0.0.1',
author='amit',
author_email='amit3169@gmail.com',
packages=find_packages(),
install_requires=get_requirements(),

)