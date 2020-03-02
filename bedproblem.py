#!/usr/bin/env python3
#author: Michele Fischer, 1.3.2020
import sys
import operator

#reading the lines and safe them as a list
kitten_times = list()
n_visiting_kitten = 0
k_spare_beds = 0

for num, input_line in enumerate(sys.stdin.readlines()):
    if num == 0:
        n_visiting_kitten, k_spare_beds = map(int, input_line.split())
        continue

    kitten_times.append(list(map(int,input_line.split())))

kitten_times.sort(key = operator.itemgetter(0, 1))

kitten_count= 0
max_kitten_all_beds = list()

#iterating through k beds
for k in range(1,k_spare_beds+1):
    max_kitten_one_bed = list()
    #iterating through the dates with comparing last y with next x
    for dates in kitten_times:
        x,y = dates
        kitten_count = 1
        for i in kitten_times[kitten_times.index(dates):]:
            compared_date = i
            x = compared_date[0]
            if y <= x:
                kitten_count += 1
                y = compared_date[1]
        max_kitten_one_bed.append(kitten_count)
    #index of the max kitten in one bed    
    max_kitten_one_bed_index =max_kitten_one_bed.index(max(max_kitten_one_bed))
    #the start of the iteration for the date with the max kitten in one bed
    reserved_bed = kitten_times[max_kitten_one_bed_index]
    max_kitten_all_beds.append(max(max_kitten_one_bed))

    x,y = reserved_bed
    #creating new list for next bed
    for i in kitten_times[max_kitten_one_bed_index:]:
        compared_date = i
        x = compared_date[0]
            
        if y <= x:
            kitten_times.remove(compared_date)
            y = compared_date[1]
    kitten_times.remove(reserved_bed)
    if kitten_times == []:
        break
#result by adding the max kitten for every bed together
max_kitten_all_beds = sum(max_kitten_all_beds)
print(max_kitten_all_beds)
