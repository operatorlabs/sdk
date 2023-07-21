from setuptools import setup, find_packages

setup(
    name="operator-search",
    version="0.1.0",
    description="A Python SDK for the Operator Search API.",
    author="David Shi",
    author_email="david@operator.io",
    url="https://github.com/operatorlabs/sdk/python",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    test_suite="tests",
)