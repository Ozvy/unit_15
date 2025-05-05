from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

'''
Consumer Price Index for Gasoline in U.S City Average
Ender Whittington
5/4/2025
'''
path = Path('CUSR0000SETB01.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, col_title in enumerate(header_row):
    print(f'{index} {col_title}, ', end=' ')


dates = []
price_index = []

for row in reader:
    try:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        index = float(row[1])
    except ValueError as e:
        print(current_date)
    else:
        dates.append(current_date)
        price_index.append(index)

figure, graph = plt.subplots()
graph.set_title('Consumer Price Index for Gasoline in U.S City Average')
graph.set_ylabel('Index Jan 2020-Dec 2020')
figure.autofmt_xdate()
graph.plot(dates, price_index, color='blue')

plt.show()