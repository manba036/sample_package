from setuptools import setup, find_packages

setup(
    name='sample_package',
    version='0.1',
    description='Sample to pip install via GitHub.',
    long_description='./README.md',
    author='Manba Osamu',
    author_email='manba@zf7.so-net.ne.jp',
    install_requires=[],
    url='https://github.com/manba036/sample_package',
    license='./LICENSE',
    packages=find_packages(),
)