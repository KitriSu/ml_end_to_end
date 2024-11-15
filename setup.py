from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = ".e ."


def get_requirements(file_path: str) -> List[str]:
    """
    return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="ml_end_to_end",
    version="0.0.1",
    author="Kitri",
    author_email="yuqingsu9@gmail.com",
    packages=find_packages(),
    install_requirements=get_requirements("requirement.txt"),
)
