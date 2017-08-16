from setuptools import setup

setup(name='gym_sudoku',
	version='0.0.4',
	install_requires=['gym'],
	description='Sudoku environment for OpenAI gym',
	license=open('LICENCE', "r").read(),
	long_description=open('README.md', "r").read(),
	keywords='sudoku,openai,gym,environment',
	author='artonge',
	author_email='artonge@chmn.me',
	url='https://github.com/artonge/sudokuEnv'
)
