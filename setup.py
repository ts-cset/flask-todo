import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="flasktodo",
    version="0.0.1",
    author="Lee Enck",
    author_email="eaglesfootball33@gmail.com",
    url="https://github.com/LeeEnck/flask-todo",
    description="A simple to-do application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=['flask', 'psycopg2'],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
