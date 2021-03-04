from setuptools import setup

major_version = 1
minor_version = 0
build_version = 0

version = str(major_version) + '.' + str(minor_version) + '.' + str(build_version)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='powerwallstats',
    version=version,
    description='powerwallstats: python library to read statistics from a Powerwall 2 gateway',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Simon Moore',
    url='https://github.com/swm11/powerwallstats',
    license='BSD 2-Clause',
    packages=('powerwallstats',),
    install_requires=('requests',),
    python_requires=">=3.6",
)
