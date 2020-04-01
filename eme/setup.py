import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EME-pkg-VINCECARSE", # Replace with your own username
    version="0.0.1",
    author="Vincent Carse",
    author_email="vincecarse@gmail.com",
    description="Tools to process data from the TEA and other sources",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vincecarse/EME",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
