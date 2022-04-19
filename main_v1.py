import argparse
from msilib.schema import Error
from multiprocessing.sharedctypes import Value
import os
import sys
import load

parser = argparse.ArgumentParser()
parser.add_argument("folder")
args = parser.parse_args()
cd = args.folder

if cd:
    try:
        with open(f"{cd}/game.csv") as x:
            lines = x.readlines
        
    except OSError:
        print(f'Folder "{cd}" tidak ditemukan.')
        exit()
    
else:
    print("Tidak ada nama folder yang diberikan!")


print(load.load_csv(f"{cd}/riwayat.csv"))
