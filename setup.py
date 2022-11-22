from setuptools import find_packages,setup
from typing import List
# Paper - https://www.sciencedirect.com/science/article/abs/pii/S0883292719300435
PROJECT_NAME = "Classification of Geochemical Data"
VERSION = "0.0.0"
AUTHOR = "Vaasu Bisht"
DESCRIPTION = """Building a classifier to create a reliable multivariate discrimination scheme for chromitites in the Bushveld Complex.The Bushveld Complex, the 
largest layered mafic-ultramafic intrusion worldwide, is host of numerous, laterally continuous and chemically similar chromitite layers. Based on their 
stratigraphic position the layers are subdivided into a lower, middle and upper group ."""
EMAIL = "bishtvaasu@gmail.com"
REQUIREMENT_FILE_NAME= "requirements.txt"

HYPHEN_E_DOT = "-e ."

def get_requirements_list() -> List[str]:
    """Function to return the list of requirnments mention in the requirements.txt file. 

    Returns:
        List[str]: List of libraries mentioned in the requirements.txt file.
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list

setup(
    name = PROJECT_NAME,
    version = VERSION,
    description = DESCRIPTION,
    packages = find_packages(),
    install_requires = get_requirements_list(),
    long_description=DESCRIPTION,
    author_email = EMAIL
)