from setuptools import setup

#Read the content from README.md file for project description
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='elxsi',
      #Currently deployed stable version: v1.0.3
      version='1.0.4',
      description='Python package for advanced mathematical operations, distributions and visualizations',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url="https://github.com/WorkspaceDevelopers/elxsi",
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
      packages=['elxsi'],
      author= 'Ashwin Raj',
      author_email= 'rajashwin733@gmail.com',
      zip_safe=False)
