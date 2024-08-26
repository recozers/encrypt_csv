from setuptools import setup, find_packages

setup(
    name='encrypt_csv',
    version='0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'encrypt-csv=encrypt_csv.cli:main',
        ],
    },
    install_requires=[],
    description='A simple command-line tool to encrypt columns in a CSV file.',
    author='Stuart Bladon',
    author_email='stuart.bladon@duke.edu',
    url='https://github.com/yourusername/encrypt_csv',  # Optional: Your project URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)