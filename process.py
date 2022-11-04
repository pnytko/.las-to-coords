import argparse
import numpy as np
import laspy
import glob, os

parser = argparse.ArgumentParser()
parser.add_argument('-i', required = True)
parser.add_argument('-o')
args = parser.parse_args()

os.chdir(args.i)
dir = glob.glob('*.las')
qty = len(dir)
name_list = []

for las_file in dir:
     name, ext = os.path.splitext(las_file)
     name_list.append(name)

for file in glob.glob("*.las"):
    entry = laspy.read(file)
    las_points = np.dstack([entry.x, entry.y])
    for i in range(1, qty):
        np.savetxt(f"{name_list[i]}_PS.xyz ", las_points[0], delimiter=" ", fmt="%f")