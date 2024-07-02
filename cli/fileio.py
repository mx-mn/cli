"""file io for csv files"""

import csv
from pathlib import Path

def __increment_version(path:Path):
    """parse the path and add or increment version"""
    while path.exists(): 
        parts = path.stem.split("_")
        if len(parts) > 1 and parts[-1].isnumeric():
            name = "".join(parts[:-1]) + f"_{int(parts[-1])+1}"
        else: name = path.stem + "_1"
        path = path.parents / f"{name}{path.suffix}"
    return path

def read(path: Path):
    """read data row wise from .csv"""
    if not path.exists(): raise 
    with open(path, mode='r') as file:
        data = [row for row in csv.reader(file)]
    return data

def write(path: Path, data):
    """write data to a"""
    path = __increment_version(path)
    with open(path, mode='w', newline='') as csvfile:
        csv.writer(csvfile).writerows(data)
