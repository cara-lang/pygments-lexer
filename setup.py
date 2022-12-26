#!/usr/bin/env python
"""Setup Pygments lexers."""
from setuptools import setup, find_packages

# Adapted from facelessuser/pymdown-lexers

entry_points = '''
[pygments.lexers]
cara=lexers:CaraLexer
'''

setup(
    name='pygments-lexer',
    version='1.0.0',
    description='Pygments lexer package for the Cara language.',
    author='Martin Janiczek',
    author_email='martin@janiczek.cz',
    url='https://github.com/cara-lang/pygments-lexer',
    packages=find_packages(),
    entry_points=entry_points,
    install_requires=[
        'Pygments>=2.0.1'
    ],
    zip_safe=True,
    license='BSD-3-Clause',
    classifiers=[]
)
