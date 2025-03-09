from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of dependencies.
    """
    hyphen = "-e ."
    requirements = []
    
    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()  # Read all lines into a list
        requirements = [req.strip() for req in requirements]  # Remove newline characters

        if hyphen in requirements:
            requirements.remove(hyphen)  # Remove "-e ." if present
    
    return requirements

setup(
    name="MLProject",
    version="0.0.1",
    author="SRIRAM VELUMURI",
    author_email="sriramvelumuri05@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)