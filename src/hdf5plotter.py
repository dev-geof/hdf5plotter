from argparse import ArgumentParser
import h5py
import yaml
import matplotlib.pyplot as plt
from puma import Histogram, HistogramPlot
from atlasify import atlasify, set_xlabel, set_ylabel
from termcolor import colored
import logging
from configuration import configure_logging, load_config, create_directory

import warnings

warnings.filterwarnings("ignore")


def hdf5plotter(configfile, outputdir):
    """
    Read configuration, extract input variables and files, and create histogram plots.

    Parameters:
        configfile (str): Path to the YAML configuration file.
        outputdir (str): Path to the output directory for saving plots.

    Returns:
        None

    """

    # configure logging module
    configure_logging()

    # Create output directory if it does not exist
    create_directory(outputdir)

    logging.info(colored("HDF5 PLOTTER", "green"))
    logging.info(colored("Extracting configuration", "yellow"))

    # List of fields to be extracted from yaml file
    with open(configfile, "r") as file:
        prime_service = yaml.safe_load(file)

    var_list = prime_service["input_variables"]
    file_list = prime_service["input_files"]

    # loop over the input variables
    for v in range(len(var_list)):
        var = var_list[v]
        var_key = list(var.keys())[0]

        xlabel = var[var_key]["xlabel"]
        ylabel = var[var_key]["ylabel"]
        nbins = var[var_key]["nbins"]
        xmin = var[var_key]["xmin"]
        xmax = var[var_key]["xmax"]
        scaling = var[var_key]["scaling"]
        norm = var[var_key]["norm"]
        log = var[var_key]["log"]
        logx = var[var_key]["logx"]
        brand = var[var_key]["brand"]
        title = var[var_key]["title"]
        tag = var[var_key]["tag"]

        # initialise Histogram plot
        plot = HistogramPlot(
            xlabel=xlabel,
            ylabel=ylabel,
            bins=nbins,
            bins_range=(xmin, xmax),
            norm=norm,
            logy=log,
            logx=logx,
            figsize=(6, 5),
            n_ratio_panels=1,
            ymax_ratio=2.0,
            ymin_ratio=0.0,
            atlas_brand=brand,
            atlas_first_tag=title,
            atlas_second_tag=tag,
            underoverflow=True,
        )

        # loop over the input files
        for f in range(len(file_list)):

            # getting input file
            file = file_list[f]
            file_key = list(file.keys())[0]

            # getting attributes
            path = file[file_key]["path"]
            dataset = file[file_key]["dataset"]
            weights = file[file_key]["weights"]
            label = file[file_key]["label"]
            colour = file[file_key]["colour"]
            linestyle = file[file_key]["linestyle"]
            histotype = file[file_key]["histotype"]

            with h5py.File(path, "r") as h5file:
                ds = h5file[dataset]

                if weights is not None:
                    hist = Histogram(
                        ds[var_key] / scaling,
                        weights=ds[weights],
                        label=label,
                        histtype=histotype,
                        colour=colour,
                        linestyle=linestyle,
                    )
                else:
                    hist = Histogram(
                        ds[var_key] / scaling,
                        label=label,
                        histtype=histotype,
                        colour=colour,
                        linestyle=linestyle,
                    )

                # set reference histogram
                if f == 0:
                    plot.add(hist, reference=True)
                else:
                    plot.add(hist)

        plot.draw()
        plot.savefig(outputdir + "/" + var_key + ".pdf")
        logging.info(colored(f"{var_key} saved", "yellow"))


def main():
    """
    Entry point for the hdf5plotter script.

    Parses command-line arguments and invokes the hdf5plotter function.
    """

    parser = ArgumentParser(description="HDF5 Plotter")
    parser.add_argument(
        "--configfile",
        action="store",
        dest="configfile",
        default="config.yaml",
        help="Path to the YAML configuration file.",
    )
    parser.add_argument(
        "--outputdir",
        action="store",
        dest="outputdir",
        default="outpudir",
        help="Path to the output directory for saving plots.",
    )

    args = vars(parser.parse_args())
    hdf5plotter(**args)


if __name__ == "__main__":
    main()
