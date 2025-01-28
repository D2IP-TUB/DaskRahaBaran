from setuptools import find_packages, setup

setup(
    name="daskrahabaran",
    version="1.0.0",
    packages=find_packages(),
    url="git@github.com:D2IP-TUB/DaskRahaBaran.git",
    license="Apache 2.0",
    description="Accelerating the Data Cleaning Systems Raha and Baran through Task and Data Parallelism",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords=[
        "Data Cleaning",
        "Machine Learning",
        "Error Detection",
        "Error Correction",
        "Data Repairing",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "numpy==1.22.0",
        "pandas==2.0.1",
        "scipy==1.7.2",
        "scikit-learn==1.2.2",
        "matplotlib==3.7.1",
        "prettytable==0.7.2",
        "mwparserfromhell==0.5.4",
        "beautifulsoup4==4.6.0",
        "py7zr==0.20.2",
        "fastcluster==1.2.6",
    ],
    extras_require={
        "dask": [
            "dask==2023.10.1",
            "distributed==2023.10.1",
            "dask[dataframe]==2023.10.1",
        ]
    },
    include_package_data=True,
)
