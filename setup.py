from setuptools import setup

setup(
    name='mpltransform',
    version='0.1',
    description='Custom transforms for matplotlib',
    url='https://github.com/alastairgarner/mpltransform',
    author='Alastair G',
    author_email='garneralastair@gmail.com',
    license='MIT',
    packages=['mpltransform'],
    install_requires=[
        'matplotlib',
    ],
    zip_safe=False
)