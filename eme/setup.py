import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bathrooms_predictor-pkg-VINCECARSE", # Replace with your own username
    version="0.0.1",
    author="Vincent Carse",
    author_email="vincecarse@gmail.com",
    description="Tools to extract the number of bathrooms from property descriptions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vincecarse/bathrooms_predictor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
