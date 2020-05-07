import setuptools

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="chessterm-sdk",
    version="0.1.1.post1",
    author="JingBh",
    author_email="jingbohao@yeah.net",
    description="ChessTerm SDK for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JingBh/chessterm-sdk-python",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    python_requires='~=3.4',
)
