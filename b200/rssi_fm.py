import os
from extract_rssi import extract_rssi
import re

spectrum = []
for root, dirs, files in os.walk("/home/joeyschwalb/PycharmProjects/SDR_DSP/IQ_data", topdown=False):
    for name in files:
        search = re.search("_",name)
        #print(name)
        path = os.path.join(root, name)
        rssi = extract_rssi(path)
        spectrum.append((name[:search.start()], rssi))
        print(spectrum[len(spectrum)-1])

print("debug")