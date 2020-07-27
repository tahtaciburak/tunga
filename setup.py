import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

try:
    build_version = str(os.environ["BUILD_VERSION"])
except:
    build_version = "local"

setuptools.setup(
    name="tunga",
    version="1.0.0." + build_version,
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
