from setuptools import find_packages , setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    with open(file_path) as file_obj:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements=[req.replace("\n","") for req in requirements ]

            if HYPEN_E_DOT in requirements:

                requirements.remove(HYPEN_E_DOT)
    return requirements 

setup(
    name='mlproject',
    version='0.0.1',
    author='Harshit',
    author_email='24ug1bycs555@bmsit.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
