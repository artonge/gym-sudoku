import setuptools

setuptools.setup(name='gym_sudoku',
	version='1.0.4',
	install_requires=['gym'],
	description='Sudoku environment for OpenAI gym',
	license=open('LICENCE', "r").read(),
	long_description=open('README.md', "r").read(),
	keywords='sudoku,openai,gym,environment',
	author='artonge',
	packages=setuptools.find_packages(),
	author_email='artonge@chmn.me',
	url='https://github.com/artonge/sudokuEnv'
)
