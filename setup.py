import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="seb-dev-libraries",
    version="0.0.1",
    author="Seb",
    author_email="wdowiarzsebastian@gmail.com",
    packages=["seb-dev-libraries"],
    description="Package to hold development dependencies.",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/mangekyousharingan/seb-dev-libraries",
    license='MIT',
    python_requires='>=3.9',
    install_requires=[]
)
