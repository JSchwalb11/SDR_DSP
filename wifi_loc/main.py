import subprocess
import os

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = 'ap2.txt'

    with open(f, 'r') as file:
        for line in file:
            print(line)