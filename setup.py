import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='Jetbrains Space Python SDK',
     version='0.1-pre-alfa',
     author="Gabriel Mourão",
     author_email="gabrielmouraodemelo@gmail.com",
     description="A Jerbrains Space Python SDK",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/AnthraxisBR/jetbrains-space-python-sdk",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )