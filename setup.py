from setuptools import setup


with open("requirements.txt", "r") as f:
    install_requires = f.readlines()
    f.close


setup(install_requires=install_requires)
