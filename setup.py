from setuptools import find_packages,setup

def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requiremnets=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

setup(
    name='mlproject',
    version='0.0.1',
    author="Sourav",
    author_email='lcs.souravkrsahu@gmail.com',
    packeges=find_packages(),
    install_requires=get_requirements('requirement.txt')
)