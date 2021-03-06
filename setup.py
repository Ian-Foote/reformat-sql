import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reformat-sql",
    version="0.0.1",
    author="Ian Foote",
    author_email="python@ian.feete.org",
    description="A tool for reformatting SQL for readability",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ian-Foote/reformat-sql",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['sqlparse'],
)
