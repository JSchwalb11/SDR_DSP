#!/bin/bash

sudo iw wlo1 scan | egrep 'SSID|signal' | tee -i ap.txt
