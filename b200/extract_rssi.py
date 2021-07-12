import numpy as np
import argparse
import uhd
import time
import json

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--args", default="", type=str)
    parser.add_argument("-o", "--output-file", type=str, default=991e5)
    parser.add_argument("-f", "--freq", type=float, required=False)
    parser.add_argument("-r", "--rate", default=4e5, type=float)
    parser.add_argument("-d", "--duration", default=1.0, type=float)
    parser.add_argument("-c", "--channels", default=0, nargs="+", type=int)
    parser.add_argument("-g", "--gain", type=int, default=40)
    parser.add_argument("--debug", default=False, type=str)
    parser.add_argument("--path", default="/home/joeyschwalb/PycharmProjects/SDR_DSP/IQ_data/", type=str)
    return parser.parse_args()

def get_iq_991_fm():
    # args = parse_args()
    num_samps=int(10e6)
    freq=991e5
    rate=4e5
    channels=[0]
    gain=40

    usrp = uhd.usrp.MultiUSRP()
    samps = usrp.recv_num_samps(num_samps, freq, rate, channels, gain)

    return samps

def extract_rssi(path="/home/joeyschwalb/PycharmProjects/SDR_DSP/IQ_data/991_fm.bin", debug=False):
    if not debug:
        file = open(path, 'r')
        signal = np.fromfile(file, dtype=np.complex64)

    if debug:
        signal = get_iq_991_fm()
        file = path
        with open(file, 'wb') as f:
            np.save(f, signal, allow_pickle=False, fix_imports=False)

    try:
        power = 10 * np.log10(signal)
        adjusted_pwr = power.real
        rssi = np.mean(adjusted_pwr)
    except RuntimeWarning:
        return None

    if not debug:
        file.close()

    return rssi



def main():
    args = parse_args()
    if args.debug == 'False':
        num_samps = int(10e6)
        freq = 991e5
        rate = 4e5
        channels = [0]
        gain = 40

        start_freq = 881
        end_freq = 1081
        step =  (1080-880)//100
        samples = dict()

        for _freq in range(start_freq, end_freq, step):
            usrp = uhd.usrp.MultiUSRP()
            start = time.time()
            signal = usrp.recv_num_samps(num_samps, freq, rate, channels, gain)
            end = time.time()
            print("Signal Sampling time taken: {0}".format(end-start))

            sig_pwr = 10*np.log10(signal)
            sig_str = np.mean(sig_pwr.real)
            sig_str_adj = sig_str - gain

            samples[_freq] = sig_str_adj
            print("Done sampling {0}MHz ({1} db)".format(
                str(_freq)[:len(str(_freq))-1]+"."+str(_freq)[len(str(_freq))-1:],
                samples[_freq])
                )

            with open(args.path + str(_freq) + ".bin", 'wb') as f:
                np.save(f, signal, allow_pickle=False, fix_imports=False)

        with open(args.path + "fm_spectrum_rssi.json", 'w') as f:
            json.dump(samples, f)

    else:
        rssi = extract_rssi(debug=args.debug)


if __name__ == "__main__":
    main()

