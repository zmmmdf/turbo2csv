from setuptools import setup, find_packages

setup(
    name='turbo2csv',
    version='1.1.0',
    description='This is a Python web scraper built to extract car information from Turbo.az, one of the most popular car purchase websites in Azerbaijan.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/zmmmdf/turbo2csv',
    author='Ziya Mammadov',
    author_email='ziyamm08@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    py_modules=['turbo2csv.scraper'],
    install_requires=[
        'selenium',
    ],
    python_requires='>=3.6',
)
