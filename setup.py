import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tunga",
    version="0.0.1",
    author="Burak TAHTACI",
    author_email="tahtaiburak@gmail.com",
    description="Tunga Core Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tahtaciburak/tunga",
    packages=setuptools.find_packages(exclude=("backend", "frontend", "experiments", "tests", "images")),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
