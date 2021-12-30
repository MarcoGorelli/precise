import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="precise",
    version="0.0.1",
    description="just playing around",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/microprediction/precise",
    author="microprediction",
    author_email="peter.cotton@microprediction.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["precise"],
    test_suite='pytest',
    tests_require=['pytest','winning>=0.4.1','scikit-learn'],
    include_package_data=True,
    install_requires=['vectorbt'],
    entry_points={
        "console_scripts": [
            "precise=precise.__main__:main",
        ]
    },
)