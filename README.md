# SDR_DSP

SDR_DSP is a collection of tools and scripts that were used in learning the basics of Software Radios and Digital Signal Processing in Python. Two radios were used to collect samples: Ettus Research B200 and ADALM Pluto Radios. GNU RADIO 3.9 was compiled from source and used for signal processing. Various out of tree modules were used while exploring new signal concepts. Rudimentary radio localization methods are implemented via RSSI on both FM and Wifi frequencies (see Mukherjee et al. for background (DOI: 10.26599/BDMA.2019.9020013).

## Installation

All software was used on Ubuntu 20.04.

Use the package manager [gnuradio](https://wiki.gnuradio.org/index.php/InstallingGR) to install GNU Radio. Install [UHD](https://github.com/EttusResearch/uhd) to use a UHD device with GNU. Install [ADALM-Pluto] OOT module to use the radio with GNU

