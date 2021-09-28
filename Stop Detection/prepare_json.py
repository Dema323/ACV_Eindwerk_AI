import re
import sys
with open('data.json',"r") as infile, open('output.json',"w") as outfile:
    outfile.write('{ "gps" : ')
    for line in infile:
        line = line.replace("\\", "")
        line = line.replace('"[', "[")
        line = line.replace(']"', "]")
        outfile.write(line)
    outfile.write("}")