import runpy
from setuptools import setup, find_packages

PACKAGE_NAME = "package-boilerplate"
version_meta = runpy.run_path("./version.py")
VERSION = version_meta["__version__"]


with open("README.md", "r") as fh:
    long_description = fh.read()


def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


if __name__ == "__main__":
    setup(
        name='wethr',
        version='0.0.1',
        packages=find_packages(),
        install_requires=parse_requirements("requirements.txt"),
        python_requires=">=3.6.3",
        scripts=["scripts/weather"],
        description="Weather.com CLI",
        long_description=long_description,
        long_description_content_type="text/markdown",
    )