# HDF5 Plotter

## Introduction

Simple package designed for creating histogram plots from data stored in HDF5 compound datasets. The script reads configuration parameters from a YAML file, specifies input files and fields, and produces histogram plots with specified cosmetic settings. Plots for each specified field are saves in the output directory as PDF files. The file names correspond to the field names.

## Getting the Code

To get started you can clone the `hdf5plotter` repository from GitHub using the following command:
```bash
git clone https://github.com/dev-geof/hdf5plotter.git
```

## Installation

To install `hdf5plotter` and its dependencies you can use the following command:
```bash
python -m pip install -e . -r requirements.txt
```

## Usage

### Script Invocation

```bash
hdf5plotter --configfile path/to/config.yaml --outputdir path/to/output/directory
```

## License

`hdf5plotter` is distributed under the [MIT License](LICENSE), granting users the freedom to use, modify, and distribute the code. Contributions, bug reports, and suggestions for improvements are warmly welcomed.
