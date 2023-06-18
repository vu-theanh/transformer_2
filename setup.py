from setuptools import setup, find_packages

setup(
    name='well_log_transformer',
    version='1.0.0',
    description='A package for well_log data transformation',
    author='The Anh Vu',
    author_email='anhthevu84@@email.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'SparkSession'
        # Add any other dependencies here
    ],
)

