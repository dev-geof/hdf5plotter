import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hdf5-plotter",
    version="0.1.0",
    author="Geoffrey Gilles",
    description="Simple plotting script for HDF5 compound dataset content",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dev-geof/hdf5-plotter",
    packages=setuptools.find_packages(),
    install_requires=[
        "h5py>=3.8.0",
        "PyYAML>=6.0",
        "matplotlib>=3.5.3",
        "puma-hep>=0.2.2",
        "atlasify>=0.8.0", 
        "termcolor>=1.1.0",

    ],
    entry_points={
        "console_scripts": [
            "hdf5plotter=src.hdf5plotter:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.9.13",
)
