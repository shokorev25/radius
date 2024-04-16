from setuptools import setup, find_packages

setup(
   name='radius',
   version='1.0',
   description='A utility that calculates the area of a circle by a given radius.',
   license='MIT',
   author='shokorev25',
   author_email='shokorev25@gmail.com',
   url='https://github.com/shokorev25/radius.git',
   packages=find_packages(),
   install_requires=[], # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)
