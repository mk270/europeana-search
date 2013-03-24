from setuptools import setup

setup(
    name='europeana-search',
    version='0.2.0',
    author='Martin Keegan',
    author_email='martin@no.ucant.org',
    packages=['europeana'],
    scripts=[],
    url='',
    license='LICENSE.txt',
    description='Basic Python wrapper for Europeana Search API.',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests >= 1.1.0"
    ],
)
