import csv
import json
import sys

#python json2csv.py results61001-100000.json output.csv
#check if you pass the input file and output file
if sys.argv[1] is not None and sys.argv[2] is not None:
    fileInput = sys.argv[1]
    fileOutput = sys.argv[2]
    inputFile = open(fileInput) #open json file
    outputFile = open(fileOutput, 'w') #load csv file
    writer = csv.writer(outputFile, delimiter =" ")
    for line in inputFile:
      d = json.loads(line)
      for key, value in d.items():
        writer.writerow([value])