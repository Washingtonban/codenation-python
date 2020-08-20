# .travis.yml
config = """
language: python
python:
  - "2.7"
  - "3.7"
  - "pypy"
  - "pypy3"
stages:
  - test
jobs:
  include:
    - stage: test
      name: Unit Tests
install:
  pip install -r requirements.txt
script: pytest
"""
