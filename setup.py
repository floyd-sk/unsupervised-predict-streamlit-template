from setuptools import setup, find_packages

setup(
    name = 'unsupervised_functions',
    version = '0.1',
    packages = find_packages(exclude=['tests*']),
    license = 'MIT',
    description = 'Movie Recommender helper functions',
    long_description = open('README.md').read(),
    install_requires = ['numpy', 'pandas', 'seaborn', 'cufflinks', 'sklearn', 'scikit-surprise'],
    url = 'https://github.com/Marth418/unsupervised-predict-streamlit-template',
    author = 'JHB_Team_RM4',
    author_email = ['floyd.skakane@gmail.com', 'christinah.chokwe@gmail.com', 'kwenadiletsoalo6@gmail.com', 'mahhembe@gmail.com', 'mbedzigudani141@gmail.com']