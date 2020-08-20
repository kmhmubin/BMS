import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Bank Management System",
    version="0.0.1",
    author="kmhmubin",
    description="A simple bank management system in python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kmhmubin/BMS",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
