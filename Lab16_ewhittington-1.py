from pathlib import Path
import csv
import matplotlib.pyplot as plt

path = Path('CUSR0000SETB01.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = csv.reader(lines)
print(header_row)