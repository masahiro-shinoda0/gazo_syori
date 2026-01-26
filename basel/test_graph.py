import matplotlib.pyplot as plt
import csv

a = []
with open("basel_output.csv") as f:
    reader = csv.reader(f)
    for i in reader:
        a[i] = i
