from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]

setup(
    name='kekw',
    version='0.0',
    description='A simple flask app',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
