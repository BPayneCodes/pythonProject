# Author: Billy Payne

import csv

# calculates distance from distance_data.csv.csv
with open('csv/distance_data.csv') as distance_csv_file:
    # pulls list from csv and parses in commas
    distance_csv = list(csv.reader(distance_csv_file, delimiter=','))

# prompts address from address_data.csv
with open('csv/address_data.csv') as address_csv_file:
    # pulls address list from csv and parses in commas
    address_csv = list(csv.reader(address_csv_file, delimiter=','))


# This function to gather floating point range between two destinations from distance_data.csv.csv file.
# Big O Time Complexity O(1)
def distance_between_addresses(x, y):
    # check distance marker
    distance = distance_csv[x][y]
    # distance search
    if distance == '':
        distance = distance_csv[y][x]
    return float(distance)


# Function to return the address number from the address string literal. O(n)
def address_number_from_string(address):
    # index search
    for i in address_csv:
        if address in i[2]:
            return int(i[0])