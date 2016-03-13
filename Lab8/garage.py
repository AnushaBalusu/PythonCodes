__author__ = 'anusha_balusu, pankhuri_roy'

"""
CSCI-603: Lab 8
Author: Anusha Balusu (ab5136@rit.edu), Pankhuri Roy (pr6538@rit.edu)
New Jobs arrive in Cathy and Harold's Garage. Cathy always does jobs in order of (max) cost
Harold always does jobs in order of (min) hours.
Two heaps:  min heap of jobs (based on hours)
            max heap (based on cost)
            list of jobs with indices of them in both heaps
"""

import sys
from heap import Heap

MINTYPE = "min" # harold min time
MAXTYPE = "max" # cathy max cost


class Job():
    __slots__ = "name", "hours", "cost", "indexMin", "indexMax"

    def __init__(self, name=None, hours=None, cost=None, indexMin=-1, indexMax=-1):
        self.name = name
        self.hours = int(hours)
        self.cost = int(cost)
        self.indexMin = indexMin
        self.indexMax = indexMax

    def __str__(self):
        ret = ""
        ret = self.name + "-" + str(self.hours) + "-" + str(self.cost) + "-" + str(self.indexMin) + "-" + str(self.indexMax)
        return ret

def compareHours(x, y):
    return x.hours < y.hours

def compareCosts(x, y):
    return x.cost > y.cost


def processFile(fileName):
    with open(fileName) as f:
        minh = Heap(compareHours)
        maxh = Heap(compareCosts)
        indexList = []
        for line in f:
            line = line.strip().split(" ")
            # if Cathy/Harold are ready
            if len(line) is 2:
                if line[0] == 'Harold':
                    item = minh.pop(indexList, MINTYPE)
                    maxh.popAt(item.indexMax, indexList, MAXTYPE)
                    print("Harold starting job " + item.name)
                else:
                    item = maxh.pop(indexList, MAXTYPE)
                    minh.popAt(item.indexMin, indexList, MINTYPE)
                    print("Cathy starting job " + item.name)
            # if new jobs arrive
            else:
                jobObject = Job(line[0], line[1], line[2])
                indexList.append(jobObject)
                print("New job arriving! Job name: " + line[0] + ", " + line[1] + " hours and $" + line[2])
                minh.insert(jobObject, indexList, MINTYPE)
                maxh.insert(jobObject, indexList, MAXTYPE)


def main():
    try:
        fileName = input("Enter file name: ")
        processFile(fileName)
    except FileNotFoundError as fe:
        print(fe, file=sys.stderr)


if __name__ == '__main__':
    main()
