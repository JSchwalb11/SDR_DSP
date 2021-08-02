#!/bin/bash

#sudo iw wlo1 scan | egrep 'SSID|signal'
#sudo iw wlo1 scan
sudo iw wlo1 scan | egrep 'SSID|signal' | tee -i ap.txt
