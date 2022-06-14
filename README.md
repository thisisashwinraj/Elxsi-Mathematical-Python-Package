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
- [elxsi.egg-info](https://github.com/thisisashwinraj/Elxsi-Mathematical-Python-Package/tree/main/elxsi.egg-info): This directory contains the package's metadata, including a PKG-INGFO, and the sources.
- [elxsi](https://github.com/thisisashwinraj/Elxsi-Mathematical-Python-Package/tree/main/elxsi): This directory contains the code for performing operations and visualizing statistical distributions.

### Build Commands
To easily install the elxsi python package, run the following command to create an egg file(python distribution format):
```
python setup.py bdist_egg
```
To create raw source distribution file for the package, run the following command in the command prompt or terminal:
```
python setup.py sdist bdist_wheel
```
Running this file creates the following sub-directories: dist, and elxsi.egg-info. Executable installer can also be created for installing the package in the Microsoft Windows environment. 
To create the executable installer, run this command:
```
python setup.py bdist_wininst
```
# User Installation and Source Code
Latest stable release of elxsi can either be downloaded from the repo or be simply installed from PyPi, using the code:
```
pip install elxsi
```
Once this package has succesfully installed, a large array of different statistical distributions can be imported from the package by specifying the name of the distribution (seprated by a ',') with first letter of each word typed in uppercase

![pip install elxsi](https://github.com/thisisashwinraj/Elxsi-Mathematical-Python-Package/blob/main/doc/gifs/elxsiReadmeGIF.gif)

### Package Development
Elxsi development takes place on [GitHub](https://github.com/thisisashwinraj/Elxsi-Mathematical-Python-Package). Please submit any bugs that you may encounter to the issue tracker with a reproducible example demonstrating the problem, in accordance with the issue templates present in ~/github folder.
    
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
    

# Contribution Guidelines
To start contributing to the project, clone the repository into your local system subdirectory using the below git code:
```
git clone https://github.com/ashwinraj-in/Kiwi.git
```
Before cloning the repository, make sure to navigate to the working subdirectory of your command line interface and ensure that no folder with same name exists. Other ways to clone the repository includes using a password protected SSH key or by using Git CLI. The changes may additionally be performed by opening this repo using GitHub Desktop

### Edit the Source Code and Make Desired Changes
To be able to make changes to the source, you may need to install and use a python IDE such as PyCharm, Microsoft VisualStudio and/or any other python interpreter. You will also require a Jupyter notebook  for working with the code snippets. The movies posters are fetched using the [TMDb's API](https://developers.themoviedb.org/3). You may create your own API by logging into TMDb developers API-3. Ensure that you are strictly following the basic coding standards while making the desired change

### Submitting a Pull Request
Before opening a Pull Request, it is recommended to have a look at the full contributing page to make sure your code complies with all the pull request guidelines. Please ensure that you satisfy the [~/checklist](https://github.com/thisisashwinraj/VerticalX-Recommendation-System/tree/main/Template%20Files/PULL_REQUEST_TEMPLATE) before submitting your PR.

Navigate to this subdirectory & check status of all files that were altered (red) by running the below code in Git Bash:
```
git status
```
Stage all your files that are to be pushed into your pull request. This can be done in two ways - stage all or some files:
```
git add .            // adds every single file that shows up red when running git status
```
```
git add <filename>   // type in the particular file that you would like to add to the PR
```

Commit all the changes that you've made and describe in brief the changes that you have made, using the command:
```
git commit -m "<commit_message>"
```
Push all of your updated work into this GitHub repo in the form of a Pull Request by running the following command:
```
git push origin main
```
All pull requests are reviewed on a monthly rolling basis. Your understanding is appreciate during this review process.

# License and Project Status
This package and other resources are distributed under GNU General Public License v3.0. This package is compatible with all operating systems. The latest released stable version of elxsi is v1.0.4 & is available to be installed on any local system for general use through pip install from [Pypi](https://pypi.org/project/elxsi/) (and other indexes) using requirement specifiers. Checkout pip documentation v21.1.1 [here](https://pip.pypa.io/en/stable/). All commit-level changes are logged in the changelog.
