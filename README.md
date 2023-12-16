# salesReport
A dashboard displaying a hypothetical sales report across teams.
# Problem
Create a Python application that will read from 3 input files and use the data within to produce 2 output 
files. The 5 filenames should be taken as command-line parameters such as the following example
*python report.py -t TeamMap.csv -p ProductMaster.csv -s Sales.csv 
--team-report=TeamReport.csv --product-report=ProductReport.csv*
# Team Map
The Team Map file is a comma-separated text file where each line contains two values: an integer 
uniquely identifying a team and the string name of the team. The unique id may be assumed to be positive. The 
string team name is not quoted and may be assumed not to contain commas or non-ASCII characters. The file 
does contain a header with the field names. An example file is as follows:

