# Author: Billy Payne

import datetime

# Shows every package ID that will be delivered early or leaves at 8:00:00
# Packages to be loaded into each truck with the deadline and special notes
first_truck_packages = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
# Current package mileage
first_truck_mileage = 0.0
# Truck departure time for hash table
first_truck_start_time = datetime.timedelta(hours=8)

# Package ID that are to be delayed and have to be on truck 2. Departs at 9:10:00
# Packages to be on truck 2
second_truck_packages = [3, 6, 18, 25, 28, 32, 33, 35, 36, 38, 39]
# Current truck 2 mileage
second_truck_mileage = 0.0
# Truck 2 departure time for hash table
second_truck_start_time = datetime.timedelta(hours=9, minutes=10)

# Package ID that have the wrong address or EOD. Truck leaves at 10:25:00
# Packages to be on truck 3
third_truck_packages = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27]
# Current truck mileage
third_truck_mileage = 0.0
# Truck 3 departure time for hash table
third_truck_start_time = datetime.timedelta(hours=10, minutes=25)


