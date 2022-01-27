import csv
import statistics
with open('data.csv', newline = '')as f:
    reader = csv.reader(f)
    data = list(reader)
data.pop(0)
new_data = []
for i in range(len(data)):
    num = data[i][2]
    new_data.append(float(num))
n = len(new_data)
total = 0
for i in new_data:
    total += i
mean = statistics.mean(new_data)
median = statistics.median(new_data)
mode = statistics.mode(new_data)
print("mean = ", mean)
print("median = ", median)
print("mode = ", mode)
