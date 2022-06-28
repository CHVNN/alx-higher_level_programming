#!/usr/bin/python3
num_combo = 0
while num_combo <= 89:
    if num_combo % 10 == 0:
        num_combo += 1 + num_combo // 10
    print("{:02d}".format(num_combo), end='\n' if num_combo == 89 else ", ")
    num_combo += 1
