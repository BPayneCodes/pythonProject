# Author: Billy Payne

# class named Package to be created


class Package:

    # Big O(1) time complexity and the package object to be initializes
    def __init__(self, package_id, address, city, state, zipcode, deadline, mass, status):
        # package id
        self.package_id = package_id
        # package address
        self.address = address
        # package city
        self.city = city
        # package state
        self.state = state
        # package areacode
        self.zipcode = zipcode
        # package end
        self.deadline = deadline
        # package weight
        self.mass = mass
        # package current position
        self.status = status
        # delivery hub package status
        self.time_left_hub = None
        # delivery time for package
        self.delivery_time = None



    # Prints package object information.Big O(1) time complexity and shows user package information
    def __str__(self):
        # print package information
        return f'{self.package_id}, {self.address}, {self.city}, {self.state}, {self.zipcode}, {self.deadline} {self.mass},' \
               f' {self.delivery_time}'