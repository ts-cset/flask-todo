import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="flasktodo",
    version="0.0.1",
    author="Thom Mondeaux and Brian Brurchett",
    author_email="Thommond@protonmail.com",
    url="https://github.com/Thommond/flask-todo",
    description="A simple to-do application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=['flask', 'psycopg2'],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
