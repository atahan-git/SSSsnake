import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SSSsnake", # Replace with your own username
    version="0.0.6",
    author="Atahan Ozturk",
    author_email="atahan012000@gmail.com",
    description="IPythonDisplayTurtles edited for my schools python courses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atahan-git/IPythonDisplayTurtle",
    packages=['SSSsnake'],
    package_data={'SSSsnake': ['levels/*.js']},
    classifiers=[
        "Framework :: IPython",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Education",
    ],
    python_requires='>=3.6',
    install_requires=['IPython', 'IPythonDisplayTurtle'],
)