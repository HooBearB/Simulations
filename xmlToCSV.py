import xml.etree.ElementTree as xml
import csv
import os



def loadXML(filename):
    tree = xml.parse(filename)
    root = tree.getroot()
    return root

def pullAllData(root):
    table = []
    for child in root:
        object = {}
        object["time"] = child.attrib["duration"]
        object["wait"] = child.attrib["waitingTime"]
        object["distance"] = child.attrib["routeLength"]
        table.append(object)
    return table

def convertToCSV(table, output):
    fields= ['time', 'wait', 'distance']
    writer = csv.DictWriter(open(output, "w"), fieldnames=fields)
    writer.writeheader()
    writer.writerows(table)


root = os.path.dirname(__file__)
name = str(input("What intersection data would you like to open? \nFormat with no spaces in camelcase.\n"))
x = 1
while x <= 5:
    file = loadXML(root + "/output/" + name + "/" + name + "Tripinfo" + str(x) + ".xml")
    data = pullAllData(file)
    convertToCSV(data, root + "/output/csvData/" + name + "/" + name + "Tripinfo" + str(x) + ".csv")
    x = x + 1

