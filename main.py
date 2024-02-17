# Author: Billy Payne
# Student ID : 010047760
# C950 Data Structures and Algorithms II

from builtins import ValueError
from distance import *
from package import Package
from hash_table import HashTable
from truck import *
import datetime
import csv

# Reads package_data.cvs and pulls information from the packages
with open('csv/package_data.csv') as package_csv_file:
    # Package list parsing
    package_csv = list(csv.reader(package_csv_file, delimiter=','))



# Creates package objects from the CSV file and loads them into the hash table. Time complexity Big O(n)
def load_package_data(filename):
    # file opener
    with open(filename) as packages:
        # reader
        package_data = csv.reader(packages, delimiter=',')

# column header for hash table
        for package in package_data:
            # Package ID
            package_ID = int(package[0])
            # Package Address
            package_address = package[1]
            # Package City
            package_city = package[2]
            # Package State
            package_state = package[3]
            # Package Area Code
            package_zipcode = package[4]
            # Package End
            package_deadline = package[5]
            # Package Weight
            package_weight = package[6]
            # Package Hub Status
            package_status = package[7]
            # column headers hash
            package = Package(package_ID, package_address, package_city, package_state, package_zipcode,
                              package_deadline, package_weight, package_status)
            # new hash table insert
            package_hash.insert_into_list(package_ID, package)


# New table
package_hash = HashTable()

# Parses package data into the newly created hash table
load_package_data('csv/package_data.csv')


# The algorithm to be chosen is Nearest neighbor, and will order packages based on closest to their present address
# The total miles travels will only be summed up when the next closest address is known
# The delivery time is also determined and kept track of as the truck moves from address to address
# Once a package is dropped off from the truck the nearest neighbor algorithm will continue until the truck inventory is delivered
# Big O Time complexity of this function is [n^3]
def nearest_neighbor(truck, mileage, start):
    # Initialization data
    current_address = '4001 South 700 East'
    total_mileage = mileage
    delivery_time = start
    # Initializes the package time_left_hub with the start time of the truck
    for i in truck:
        package = package_hash.search_list(i)
        package.time_left_hub = start
    # Determines the delivery order, updates milage and time, and removes packages from the truck
    while len(truck) > 0:
        start_package = package_hash.search_list(truck[0])
        closest_distance = float(distance_between_addresses(address_number_from_string(current_address),
                                                            address_number_from_string(start_package.address)))
        closest_package_id = truck[0]
        for i in truck:
            next_package = package_hash.search_list(i)

            distance = float(distance_between_addresses(address_number_from_string(current_address),
                                                        address_number_from_string(next_package.address)))
            if distance < closest_distance:
                closest_distance = distance
                closest_package_id = i
        nearest_package = package_hash.search_list(closest_package_id)
        current_address = nearest_package.address
        total_mileage += closest_distance
        delivery_time += datetime.timedelta(hours=closest_distance / 18)
        nearest_package.delivery_time = delivery_time
        truck.remove(closest_package_id)


    return total_mileage


# Gets total mileage between all 3 trucks
# Total mileage of first truck
mileage1 = nearest_neighbor(first_truck_packages, first_truck_mileage, first_truck_start_time)
# Total mileage of second truck
mileage2 = nearest_neighbor(second_truck_packages, second_truck_mileage, second_truck_start_time)
# Total mileage of third truck

mileage3 = nearest_neighbor(third_truck_packages, third_truck_mileage, third_truck_start_time)
# Sum of all three trucks
total_mileage = mileage1 + mileage2 + mileage3

# This is where the program starts when the user runs the program.
if __name__ == '__main__':
    # Print first line of text along with total mileage
    print(f"\nWelcome to my project for Data Structures and Algorithms II (WGUPS delivery service). The total mileage "
          f"for"
          f" today's deliveries"
          f" is {total_mileage} miles. Please select an option from the menu below for more information or to "
          f"exit the program. \n")


    exit_program = True
    # User will use this prompted menu to interact with program
    while exit_program:
        print('=' * 75)
        print('1. See every package and status of every delivery at a entered time')
        print('2. See a selected package and monitor delivery status at a entered time')
        print('3. Terminate the program (Goodbye!)')
        print('=' * 75)

        # Prevents user from using any other number than what is specified from the program and throws out alert
        user_input = input('\nPlease choose from one of the numeric options above! : ')

        # Displays all package info according to input time
        if user_input == '1':
            try:
                input_time = input('\nPlease submit a time to check the status of the packages. (12 hour format: HH:MM:SS): ')
                print('')
                # time format input
                (hrs, mins, secs) = input_time.split(':')
                # variable date timetable conversion
                user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                # flips through index packages and pulls status based on time
                for i in range(1, 41):
                    # package id search key
                    package_info = package_hash.search_list(i).package_id
                    # package hub time search key
                    package_hub_time = package_hash.search_list(i).time_left_hub
                    # package deadline search key
                    package_deadline_time = package_hash.search_list(i).deadline
                    # package delivery time search key
                    package_delivery_time = package_hash.search_list(i).delivery_time
                    # package current address key
                    package_address = package_hash.search_list(i).address
                    # package city key
                    package_city = package_hash.search_list(i).city
                    # package state key


                    #change address at 10:25:00 a.m.
                    if user_time >= datetime.timedelta(hours=int(10), minutes=int(25), seconds=int(00)):
                        package = package_hash.search_list(9)
                        package.address = '410 S State St'
                    else:
                        package = package_hash.search_list(9)
                        package.address = '300 State St'



                    package_state = package_hash.search_list(i).state
                    # package area code key search
                    package_zip = package_hash.search_list(i).zipcode
                    # package time and information and details en route delivery status
                    package_weight = package_hash.search_list(i).mass
                    if package_hub_time < user_time < package_delivery_time:
                        print(f'Package ID #{package_info} -- {package_address}, {package_city}, {package_state}'
                              # en route print
                              f' , Weight {package_weight} --'
                              f' , Deadline Time {package_deadline_time} --'
                              f' , Area Code {package_zip} -- EN ROUTE.')
                        # if package hasn't left the hub yet.
                    elif user_time < package_hub_time:
                        # AT HUB print
                        print(f'Package ID #{package_info} -- {package_address}, {package_city}, {package_state}'
                              f' , Weight {package_weight} --'
                              f' , Deadline Time {package_deadline_time} --'
                              f' , Area Code {package_zip} -- AT HUB.')
                        # package delivery information

                    else:
                        print(f'Package ID #{package_info} -- {package_address}, {package_city}, {package_state}'
                              f' , Weight {package_weight} --'
                              f' , Deadline Time {package_deadline_time} --'
                              # delivered print and included address/zipcode
                              f' , Area Code {package_zip} -- DELIVERED at {package_delivery_time}.')
                print('')
                # prevents any package errors breaking the program
            except ValueError:
                print('The entry entered is invalid. Returning to Main Menu...\n')
        # Will output only one package with package ID and inputted time
        elif user_input == '2':
            # try branch with second option in menu to see a certain package and delivery time
            try:
                input_time = input('\nEnter a time to check the status of a package. (12 hour format: HH:MM:SS): ')
                # time format
                (hrs, mins, secs) = input_time.split(':')
                user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                find_package_by_id = int(input('\nInput the ID of a Package you wish to view: '))
                # ID package indexes
                if 41 > find_package_by_id > 0:
                    # package info search by ID
                    package_info = package_hash.search_list(find_package_by_id).package_id
                    # package hub time and time left search key
                    package_hub_time = package_hash.search_list(find_package_by_id).time_left_hub
                    # package deadline time search key
                    package_deadline_time = package_hash.search_list(find_package_by_id).deadline
                    # package estimated delivery time search key
                    package_delivery_time = package_hash.search_list(find_package_by_id).delivery_time
                    # package address search key
                    package_address = package_hash.search_list(find_package_by_id).address
                    # package city location search key
                    package_city = package_hash.search_list(find_package_by_id).city
                    # package state location search key
                    package_state = package_hash.search_list(find_package_by_id).state
                    # package area code search key
                    package_zip = package_hash.search_list(find_package_by_id).zipcode
                    package_weight = package_hash.search_list(find_package_by_id).mass
                    # parameter for package locations and certain prints to be displayed based on package information
                    if package_hub_time < user_time < package_delivery_time:
                        print(f'\nPackage ID #{package_info} -- {package_address}, {package_city}, {package_state}'
                              # En route branch print
                              f' , Area Code {package_zip} -- EN ROUTE.\n')
                    elif user_time < package_hub_time:
                        print(f'\nPackage ID #{package_info} -- {package_address}, {package_city}, {package_state}'
                              # At hub branch print
                              f' , Area Code {package_zip} -- AT HUB.\n')
                    else:
                        print(f'\nPackage ID #{package_info} -- {package_address}, {package_city}, {package_state}'
                              # delivery branch print
                              f' , Area Code {package_zip} -- DELIVERED at {package_delivery_time}.\n')
                else:
                    print('\nThis is an non-acceptable entry. Going back to Main Menu.\n')
                    continue
            except ValueError:
                print('\nThis is an non-acceptable entry. Going back to Main Menu.\n')
        # Terminates software
        elif user_input == '3':
            exit_program = False
            print('\n This is the end of the program. Goodbye!')
            exit()
        else:
            print('\n Unknown error. Please select a valid option from the list.\n')

