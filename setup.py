#!/usr/bin/env python3
from setuptools import setup

if __name__ == '__main__':
    setup(name='pyinfra-formulas',
          version='0.0.4',
          description='Collection of Pyinfra modules for common use cases',
          author='Hugo Herter',
          author_email='contact@hugoherter.com',
          url='https://github.com/hoh/pyinfra-formulas',
          packages=['formulas', 'formulas.nginx', 'formulas.nodejs'],
          package_dir={'formulas': 'formulas'},
          package_data={'formulas': ['*/files/*']},
          install_requires=['pyinfra', 'hereby'],
          license='MIT',
          keywords="pyinfra configuration management formulas",
          classifiers=['Development Status :: 2 - Pre-Alpha',
                       'Intended Audience :: Developers',
                       'Intended Audience :: System Administrators',
                       'License :: OSI Approved :: MIT License',
                       'Operating System :: OS Independent',
                       'Programming Language :: Python :: 3',
                       'Topic :: System :: Systems Administration',
                       ],
          )
