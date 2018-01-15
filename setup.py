import os
from setuptools import setup
from setuptools import find_packages


setup(
        name='Cape',
        version='2.0.0',
        author='Giovanni Blu Mitolo <gioscarab@gmail.com>, Colin T.A. Gray <colinta@gmail.com>',
        author_email='gioscarab@gmail.com',
        url='https://github.com/colinta/Cape.py',
        install_requires=[],

        entry_points={
            'console_scripts': [
                'cape = cape.__main__:run'
            ]
        },

        description='An implementation of Cape in Python.',
        long_description='An implementation of Cape in Python.\n\nThe included commandline utility `cape` can be used as a quick way to encrypt/decrypt/hash text.',

        packages=find_packages(exclude=['cape.tests']),
        keywords='crypt',
        platforms='any',
        license='BSD',
        classifiers=[
            'Programming Language :: Python',
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',

            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',

            'Topic :: Security :: Cryptography',
        ],
    )
