from setuptools import setup, find_packages

setup(
    name='turbo2csv',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'selenium',
    ],
    entry_points={
        'console_scripts': [
            'turbo2csv=turbo2csv.scraper:main',
        ],
    },
)
