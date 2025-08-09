'''
The setup.py file is an essential part of packaging and distributing Pythin projects. It is used to setuptools to define
the configuration of the projectm such as its metadata, dependancies and more.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function returns list of requirements
    '''
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                #ignore the empty lines and "-e ."
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not found")

    return requirement_list

setup(
    name="Network Security",
    version="0.0.0.1",
    author="Maaz",
    author_email="maaz161200@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)