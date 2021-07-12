#!/bin/bash

uhd_rx_cfile -f 881e5 -r 4e5 -N 1000000000 88_1_fm.bin
uhd_rx_cfile -f 883e5 -r 4e5 -N 1000000000 88_3_fm.bin
uhd_rx_cfile -f 885e5 -r 4e5 -N 1000000000 88_3_fm.bin
uhd_rx_cfile -f 887e5 -r 4e5 -N 1000000000 88_3_fm.bin
uhd_rx_cfile -f 889e5 -r 4e5 -N 1000000000 88_3_fm.bin
uhd_rx_cfile -f 913e5 -r 4e5 -N 1000000000 88_3_fm.bin
uhd_rx_cfile -f 883e5 -r 4e5 -N 1000000000 88_3_fm.bin

uhd_rx_cfile -f 100e5 -r 5e6 -N 1000000000 100_5_fm.bin
uhd_rx_cfile -f 105e5 -r 5e6 -N 1000000000 105_5_fm.bin

