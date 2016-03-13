__author__ = 'anusha_balusu, pankhuri_roy'

"""
CSCI-603: Lab9
Author: Anusha Balusu (ab5136@rit.edu), Pankhuri Roy (pr6538@rit.edu)

An implementation of Field of Dreams. A field has cows and paint balls.
When a paint ball explodes:
 - if cow is present in its radius, it gets colored.
 - if another paintball is present in its radius, it also explodes and process repeats
"""

import sys
import math
import copy
from graph import Graph


class FieldObject():
    """
    Field object is either a cow or paintball present in the field
    :slot: type (String) : type of object - cow / paintball
    :slot: name (String) : name of cow / color of paintball
    :slot: x (int) : x coordinate of cow / paintball
    :slot: y (int) : y coordinate of cow / paintball
    :slot: radius (int) : radius of ball. For cow, it is set as 0
    """

    __slots__ = "type", "name", "x", "y", "radius"

    def __init__(self, type, name, x=0, y=0, radius=0):
        """
        Initialize the field object
        :param type: cow / paintball
        :param name: name of cow / color of paintball
        :param x: x coordinate of cow / paintball
        :param y: y coordinate of cow / paintball
        :param radius: radius of ball. For cow, it is set as 0
        :return: None
        """
        self.type = type
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.radius = int(radius)

    def __str__(self):
        """
        Returns a string representation of the field object with all its slots
        :return: The string
        """
        ret = ""
        ret = self.type + "-" + self.name + "-" + str(self.x) + "-" + str(self.y) + "-" + str(self.radius)
        return ret

    def withinRadius(self, obj):  # self is of type paintball
        """
        Checks if the obj lies within the radius of self
        :param obj: paintball
        :return: True if obj lies within self's radius. False otherwise
        """
        ret = False
        distance = math.sqrt( ((self.x - obj.x)*(self.x - obj.x)) + ((self.y - obj.y)*(self.y - obj.y)) )
        if distance <= self.radius:
            ret = True
        return ret


def triggerPaintball(field, item, cowsDict, visitedPaintballs):
    """
    Recursively triggers paint balls or cows present within the radius of a paint ball
    :param field: the field graph
    :param item: paint ball which just got triggered
    :param cowsDict: dictionary of cows
    :param visitedPaintballs: paintballs already triggered
    :return: most overall paint, dictionary of cows ( { cow name: list of colors on the cow } )
    """
    noOfColors = 0
    for nbrItem in field.getVertex(item).getConnections():
        tempObj = nbrItem.id
        # print(tempObj)
        if tempObj.type == "paintball" and tempObj.name not in visitedPaintballs:
            # if paint ball and not visited
            visitedPaintballs.append(tempObj.name)
            print("\t" + tempObj.name + " paint ball is triggered by " + item.name + " paint ball")
            # recursive call
            noOfColors1, cowsDict = triggerPaintball(field,tempObj, cowsDict, visitedPaintballs)
            noOfColors += noOfColors1
        elif tempObj.type == "cow":
            print("\t" + tempObj.name + " is painted " + item.name + "!")
            noOfColors += 1
            # store the colors fallen on the cow
            if item.name not in cowsDict[tempObj.name]:
                cowsDict[tempObj.name].append(item.name)

    return noOfColors, cowsDict


def beginSimulation(field, cowsDict1):
    """
    Begin simulation. Trigger each ball in the field followed by chain reaction of triggering other balls
    :param field: the field graph
    :param cowsDict1: dictionary of cows for tracking the colors on each cow.
    :return: None
    """
    print("\nBeginning simulation...")
    maxColors = 0
    maxColorName = ""
    maxCowColorDetails = {}

    for item in field.getVertices():
        if item.type == "paintball":
            # copy dict by value
            cowsDict = copy.deepcopy(cowsDict1)
            print("Triggering "+ item.name + " paint ball...")
            colorCount, cowsColors = triggerPaintball(field,item,cowsDict, [item.name])
            # store details related to max overall paint colors for printing
            if maxColors < colorCount:
                maxColors = colorCount
                maxColorName = item.name
                maxCowColorDetails = cowsColors

    print("\nResults:")
    if maxColors == 0:
        print("No cows were painted by any starting paint ball!")
    else:
        print("Triggering the " + maxColorName + " paint ball is the best choice with " + str(maxColors) + " total paint on the cows:")
        for key in maxCowColorDetails:
            print("\t %s's colors: %s" % (key, maxCowColorDetails[key]))


def buildGraph(fieldObjList):
    """
    Build a directed graph of the objects in the field
    :param fieldObjList (List of FieldObject): list of objects present in the field
    :return: field graph, dictionary of all cows (used during simulation)
    """
    field = Graph()
    cowsDict = {} # is of the format { cow1: [color1, color2], cow2: [color1] }

    for index in range(0,len(fieldObjList)):
        if fieldObjList[index].type == "paintball":
            isEdgePresent = False
            for item in fieldObjList:
                if fieldObjList[index] != item and fieldObjList[index].withinRadius(item):
                    field.addEdge(fieldObjList[index], item)
                    isEdgePresent = True
            if not isEdgePresent: # add paintball as vertex if it is not connected to any other field object
                field.addVertex(fieldObjList[index])
        else:
            field.addVertex(fieldObjList[index])  # add cow as vertex
            cowsDict[fieldObjList[index].name] = []

    print("Field of Dreams")
    print("---------------")
    for obj in field:
        print(obj)

    return field, cowsDict


def processFile(fileName):
    """
    Reads file line by line and creates a list of objects(cows/paintballs) present in the field
    Then builds a graph out of the list
    :param fileName: name of file (String)
    :return: field graph, dictionary of all cows (used during simulation)
    """
    try:
        with open(fileName) as f:
            fieldObjList = []

            for line in f:
                line = line.strip().split(" ")
                if len(line) == 5:
                    fieldObjList.append(FieldObject(line[0], line[1], line[2], line[3], line[4]))
                elif len(line) == 4:
                    fieldObjList.append(FieldObject(line[0], line[1], line[2], line[3]))

            field, cowsDict = buildGraph(fieldObjList)
            return field, cowsDict

    except FileNotFoundError as fe:
        # print(fe, file=sys.stderr)
        print("File not found: "+fileName)


def main(argv):
    """
    A test function for field of dreams
    :param argv: sample input file
    :return: None
    """
    try:
        # process file and build graph
        field, cowsDict = processFile(argv[0])
        # Trigger paintballs and find the most overall paint
        beginSimulation(field, cowsDict)
    except Exception:
        print("Usage: python3 holicow.py {fileName}")


if __name__ == '__main__':
    main(sys.argv[1:])