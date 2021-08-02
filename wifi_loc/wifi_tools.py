import subprocess
import os




if __name__ == "__main__":
    f = 'ap.txt'
    command = "{0}/script.sh >> {0}}"
    print(command)
    p = subprocess.run(command)
    print("P:{0}".format(p))
    with open(f,'r') as file:
        for line in file:
            print(line)