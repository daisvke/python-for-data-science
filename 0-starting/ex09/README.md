# ft_package

This is a sample test package for learning purposes.

## Features

- A function `count_in_list` that counts occurrences of a value in a list.

## Installation

You can install the package with the following command:

```bash
# Install necessary tools (if you don't have them already)
pip install setuptools wheel

# Build the Package to create the distribution files (wheel and tar.gz)
python setup.py sdist bdist_wheel

# Install the Package
pip install ./dist/ft_package-0.0.1.tar.gz  # or the .whl file

# Verify package information
pip show -v ft_package

# Test the package
python tester.py

# Uninstall the package
pip uninstall ft_package
```

## Notes
* The setup.py file contains metadata about your package and allows it to be installed via pip.
* The MANIFEST.in file tells setuptools what files to include in the package that are not automatically included.

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
```
