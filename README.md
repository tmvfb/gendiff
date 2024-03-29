# gendiff 
[![Actions Status](https://github.com/tmvfb/gendiff/workflows/hexlet-check/badge.svg)](https://github.com/tmvfb/gendiff/actions)
[![Github Actions Status](https://github.com/tmvfb/gendiff/workflows/Python%20CI/badge.svg)](https://github.com/tmvfb/gendiff/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/9fea815a213b2c5a2a47/maintainability)](https://codeclimate.com/github/tmvfb/gendiff/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/9fea815a213b2c5a2a47/test_coverage)](https://codeclimate.com/github/tmvfb/gendiff/test_coverage)

### Tools used

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | "Python dependency management and packaging made easy"  |
| [CodeClimate Quality](https://codeclimate.com/)                             | "Your single solution for code quality"                 |
| [Flake8](https://flake8.pycqa.org/en/latest/)                               | "Your tool for style guide enforcement"                 |
| [pytest](https://docs.pytest.org/en/7.2.x/)                                 | "pytest: helps you write better programs"               |
| [GitHub Actions](https://github.com/features/actions)                       | "Automate your workflow from idea to production"        |


### Description
The package contains Linux CLI application that generates diff between two files with either **flat** or **nested** structure.  
*Application builds diff in the form of python dict of dicts via recursive search algorithm, and provides an output in the desired format.*
  
<a href="https://asciinema.org/a/cL2PWqKeUGI0vsZMf6usSO1Nk" target="_blank"><img src="https://asciinema.org/a/cL2PWqKeUGI0vsZMf6usSO1Nk.svg" style="width:700px;height:467px;" /></a>  
  
Supported input formats: 
1. json ([demo with default output format](https://asciinema.org/a/hdMWhoNNiCLTLfDyKSLi10bvw))
2. yaml ([demo with default output format](https://asciinema.org/a/fn2vOp9su5P4BUe18xHzFltAa))
  
Output formats:
1. stylish (default format, [demo](https://asciinema.org/a/5NUMVg7zXdQdOK0eIDP5rUMbl))
2. plain ([demo](https://asciinema.org/a/vA5rDhTsOnxr6Jkkl1JyRGJ8P))
3. json ([demo](https://asciinema.org/a/SX1dRffpnIVYsbL5CUj9K2Irn))


### Prerequisites
* Linux or WSL
* git
* Python >=3.8.1
* pip >=19.0
* poetry >=1.2.0

### Installation and usage

1. `git clone https://github.com/tmvfb/gendiff.git`
2. `cd gendiff`
3. `make install`
  
Check if app is properly installed by running the following in the command line: 
```sh
show_diff -f stylish ./tests/fixtures/tree1.yaml ./tests/fixtures/tree2.yml
```  
  
Type `show_diff -h` for help.  
For different output formats use following commands:
* `show_diff -f stylish file1 file2`
* `show_diff -f plain file1 file2`
* `show_diff -f json file1 file2`

### Acknowledgements

Made as a project for [hexlet.io](https://ru.hexlet.io/) python course.
