# Sudoku

An OpenAI gym environment for sudoku.


# Install
`pip install sudokugymenv`


# Release
Make sur to change `<version>` with the correct number
```shell
python setup.py bdist_wheel --universal # Build package
gpg --detach-sign -a dist/sudokuGymEnv-<version>-py2.py3-none-any.whl # Sign package
twine upload dist/* # Upload package and signature
```
