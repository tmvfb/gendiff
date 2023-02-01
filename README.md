# gendiff (hexlet.io python course)
### Hexlet tests and linter status:
[![Actions Status](https://github.com/tmvfb/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/tmvfb/python-project-50/actions)
[![Github Actions Status](https://github.com/tmvfb/python-project-50/workflows/Python%20CI/badge.svg)](https://github.com/tmvfb/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/8fac4dea5b719096bb86/maintainability)](https://codeclimate.com/github/tmvfb/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8fac4dea5b719096bb86/test_coverage)](https://codeclimate.com/github/tmvfb/python-project-50/test_coverage)

### Tools used

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | "Python dependency management and packaging made easy"  |
| [CodeClimate Quality](https://codeclimate.com/)                             | "Your single solution for code quality"                 |
| [Flake8](https://flake8.pycqa.org/en/latest/)                               | "Your tool for style guide enforcement"                 |
| [pytest](https://docs.pytest.org/en/7.2.x/)                                 | "pytest: helps you write better programs"               |
| [GitHub Actions](https://github.com/features/actions)                       | "Automate your workflow from idea to production"        |


### Description
The package contains CLI application that generates diff between two files with either **flat** or **nested** structure.  
*Application recursively builds dict of python dicts containing diff between two files, and provides an output in the desired format.*
  
Supported input formats: 
1. json ([demo with default output format](https://asciinema.org/a/hdMWhoNNiCLTLfDyKSLi10bvw))
2. yaml ([demo with default output format](https://asciinema.org/a/fn2vOp9su5P4BUe18xHzFltAa))
  
Output formats:
1. stylish (default format, [demo](https://asciinema.org/a/5NUMVg7zXdQdOK0eIDP5rUMbl))
2. plain ([demo](https://asciinema.org/a/vA5rDhTsOnxr6Jkkl1JyRGJ8P))
3. json ([demo](https://asciinema.org/a/SX1dRffpnIVYsbL5CUj9K2Irn))


### Prerequisites
* Python >=3.8.1
* pip >=19.0
* poetry >=1.2.0

### Installation
Clone repository, then `$ make install`. Installed app can be used via command line, type `gendiff -h` for help.
