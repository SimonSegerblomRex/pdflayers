#!/usr/bin/env python3
"""Setup."""
import setuptools


def _readme():
    with open('README.md', 'r') as file:
        return file.read()


setuptools.setup(
    name='pdflayers',
    version='0.1.1',
    author='Simon Segerblom Rex',
    description='PDF layer handling.',
    long_description=_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/SimonSegerblomRex/pdflayers',
    license='MIT',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'pdflayers = pdflayers.__main__:main',
        ],
    },
    python_requires='>=3.5',
    install_requires=[
        'pikepdf',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
