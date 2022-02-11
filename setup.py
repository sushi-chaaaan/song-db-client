from urllib import request
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="song-db-client",
    version="0.1.0",
    author="sushi-chaaaan",
    author_email="sushi_code@outlook.jp",
    description="A client to get data from SongDB SpreadSheet.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sushi-chaaaan/song-db-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests>=2,<3"],
    python_requires=">=3.7",
)
