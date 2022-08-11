import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="sendMail",
    version="1.0.0",
    description="Sends an email from the command line",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/scgrn/sendMail",
    author="Andrew Krause",
    author_email="ajkrause@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["sendMail"],
    include_package_data=True,
    install_requires=["win32com.client"],
    entry_points={
        "console_scripts": [
            "sendMail=sendMail.__main__:main",
        ]
    },
)
