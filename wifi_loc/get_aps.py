import subprocess
import pandas
import hashlib
import re
import uuid
from pathlib import Path


def scan_for_aps():
    password = b'qwerty1234\n'

    proc = subprocess.Popen(['/home/joeyschwalb/PycharmProjects/wifi_loc/script.sh'],
                            shell=True, stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE).communicate(input=password)


def extract_aps(path_to_file):

    re_sig = re.compile('(signal: )')
    re_SSID = re.compile(('SSID: '))

    names, power, uuids = [], [], []
    with open(path_to_file, 'r') as infile:
        for i, line in enumerate(infile):
            sig = re.search(re_sig, line)
            SSID = re.search(re_SSID, line)
            if sig:
                sig_pwr = float(line[sig.end():len(line) - 5])
                power.append(sig_pwr)
                # print("Signal Power: {0}".format(sig_pwr))
            elif SSID:
                name = line[SSID.end():len(line) - 1].encode(('utf-8'))
                names.append(name)
                #uuids.append(uuid.uuid4())


    access_points = []
    for i in range(0, len(names)):
        if power[i] > -60:
            #access_points.append((names[i], power[i], uuids[i]))
            access_points.append((names[i], power[i]))

    sorted_access_points = sort_ap_tuple(access_points)
    sorted_access_points.reverse()  # in-place reversal

    df = pandas.DataFrame(sorted_access_points, columns=["Names", "Power"]) #, "UUID"])

    return df


def avg_rssi(old_df, new_df):
    return (old_df + new_df) / 2




def check_file_size(fp):
    while Path(fp).stat().st_size == 0:
        pass
    #print("File found, size: {0}".format(Path(fp).stat().st_size))
    return

def sort_ap_tuple(tup):
    tup.sort(key=lambda x: x[1])
    return tup


if __name__ == "__main__":
    fp = "/home/joeyschwalb/PycharmProjects/wifi_loc/ap.txt"
    of = "/home/joeyschwalb/PycharmProjects/wifi_loc/filtered_ap.txt"

    old_hash = hashlib.md5(b'hello world')
    new_hash = None
    frame_count = 0
    seen_df = pandas.DataFrame(columns=["Names", "Power"])

    while True:
        check_file_size(fp) # will wait until file exists
        with open(fp, 'rb') as f:
            new_hash = hashlib.md5(f.read())

        if new_hash.digest() != old_hash.digest():
            visible_ap_df = extract_aps(fp)
            frame_count += 1
            old_hash = new_hash
            visible_ap_df.to_csv(of)

            #if df.shape == df1.shape:
            #    df1 = avg_rssi(df, df1)
            #print(df)
            #print(df1)


