from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements] #removes "\n" from readlines execution

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
name='ml_project',
version='0.0.1',
author='avik sarkar',
author_email='mail.aviksarkar@gmail.com',
packages=find_packages(),
# install_requires=['pandas', 'seaborn', 'numpy'], 
install_requires=get_requirements('requirements.txt')
)
