# Elxsi - Python Package
![](https://img.shields.io/pypi/pyversions/elxsi?color=yellow)
![](https://img.shields.io/github/license/WorkspaceDevelopers/elxsi) 
![](https://img.shields.io/bundlephobia/min/python)
![](https://img.shields.io/pypi/v/elxsi?color=magenta)
![](https://img.shields.io/pypi/wheel/elxsi)
![](https://img.shields.io/librariesio/sourcerank/Pypi/elxsi)
![](https://img.shields.io/github/issues-closed/WorkspaceDevelopers/elxsi?color=yellow)

Elxsi is a python package for performing advanced mathematical operations, distributions, and visualizations, and is licensed under the [GNU General Public License v3.0](https://github.com/thisisashwinraj/Elxsi-Mathematical-Python-Package/blob/main/LICENSE). It includes modules for calculating mean, standard deviation & probability distribution function of various statistical distributions. The latest released stable version of elxsi is v1.0.4

This project was started in 2021 by [Ashwin Raj](https://www.github.com/thisisashwinraj), as an academic project. The resources for this package, and the pull requests are maintained, and reviewed by a team of volunteers from Workspace. Learn more about elxsi v1.0.4 [here](https://pypi.org/project/elxsi/)


# Subdirectories and Constraints
### Dependencies
- Python (>= 3.9.0)
- NumPy (>=1.20.3)

**Note:**
Elxsi runs on all operating systems, is quick to install, and is available for free use. No version of elxsi supports Python 2.7, and Python 3.4. Elxsi plotting capabiliies requires matplotlib (>= 2.1.1), and seaborn (>= 0.9.0) packages.

### Files and Folders
The files and folders used in the package are as follows:
- [dist](https://github.com/thisisashwinraj/Elxsi-Mathematical-Python-Package/tree/main/dist): This directory contains the source distribution for the package, that needs to be uploaded to PyPi.
- [elxsi.egg-info](https://github.com/thisisashwinraj/Elxsi-Mathematical-Python-Package/tree/main/elxsi.egg-info): This directory contains the package's metadata including PKG-INGFO and the sources.
- [elxsi](https://github.com/thisisashwinraj/Elxsi-Mathematical-Python-Package/tree/main/elxsi): This directory contains the code for performing operations and visualizing statistical distributions.

### Build Commands
To easily install the elxsi python package, run the following command, to create an egg file (distribution format for python):
```
python setup.py bdist_egg
```
To create the raw source distribution file for this package, run the following command in the command prompt or terminal:
```
python setup.py sdist bdist_wheel
```
Running this file creates the following subdirectories: dist and elxsi.egg-info. Executable installer can also be created for installing the package in a Microsoft Windows environment. 
To create an executable installer, run this command:
```
python setup.py bdist_wininst
```
# User Installation and Source Code
The latest stable release of elxsi can either be  downloaded from this repo, or be simply installed from PyPi, using the code:
```
pip install elxsi
```
Once this package is succesfully installed, a large array of different statistical distributions can be imported from the package by specifying the name of the distribution (seprated by a ',') with first letter of each word typed in uppercase.

![pip install elxsi](https://github.com/thisisashwinraj/Elxsi-Mathematical-Python-Package/blob/main/doc/gifs/elxsiReadmeGIF.gif)

### Package Development
Elxsi development takes place on [GitHub](https://github.com/thisisashwinraj/Elxsi-Mathematical-Python-Package). Please submit any bugs that you may encounter to the issue tracker with a reproducible example demonstrating the problem, in accordance with the issue template present in /.github folder.
    
    ├── LICENSE                   // GNU General Public License v3.0
    ├── pyproject.toml
    ├── README.md                 // Contains base level documentation
    ├── setup.cfg
    ├── doc                       // Contains visual graphics (Images/Videos)
    │   └── images/Video/gif 
    ├── example                   // Contains user guide for working with elxsi
    │   └── notebook
    ├── setup.py                  // Packaged & distributed with disutils
    ├── elxsi/
    │   ├── distributions         // Code for statistical distributions
    │   └── __init__.py
    └── tests/                    // Files for performing various unit tests (To be added)
    
# Contribution
New contributors of all experience levels are welcomed to contribute to this py-project. Some basic information about the project has been included in this README. For major changes, it is recommended that you open an issue first (in line with the issue template) to discuss what you would like to change in it. Learn more about how to use elxsi [here](https://pypi.org/project/elxsi/)

### Clone the repository
To contribute to this project, clone the repository to your local directory using the below mentioned code:
```
git clone https://github.com/WorkspaceDevelopers/elxsi.git
```
### Installing Required Libraries
Install the dependencies, present in the requirements.txt file using the below mentioned code:
```
sudo pip3 install -r requirements.txt
```
### Testing the Package
After installation, you can launch the test suite from outside the source directory (requires pytest >= 3.3.0)
```
pytest elxsi
```
View statistics for elxsi via [Libraries.io](https://libraries.io/pypi/elxsi), or by using the [public dataset on Google BigQuery](https://packaging.python.org/guides/analyzing-pypi-package-downloads/).

### Submitting a Pull Request
Before opening a Pull Request, it is recommended to have a look at the full contributing page to make sure your code complies with our pull request guidelines. Please ensure that your PR satisfies the checklist before submitting.

Pull requests are reviewed by the team on a rolling basis. If we are slow to review, either the pull request needs some benchmarking, tinkering, convincing, etc. We ask for your understanding during the review process.

# License and Project Status
The package and other resources are distributed under GNU General Public License v3.0. The package is compatible with all operating systems. The latest released stable version of elxsi is v1.0.4, available to be installed on any local system for general use through pip install from [Pypi](https://pypi.org/project/elxsi/) (and other indexes) using requirement specifiers. Checkout pip documentation v21.1.1 [here](https://pip.pypa.io/en/stable/). All commit-level changes are logged in the changelog.
