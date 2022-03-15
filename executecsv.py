#Import the csv library
import csv

# list to append our records
records=[]
# open the csv file in read format
with open("info.csv",'r') as our_file:
    # use the reader object from csv library to read the file
    reader = csv.reader(our_file)
    # extract the field names
    rowheader = next(reader)
    # extract records
    for row in reader:
        records.append(row)

print(rowheader) # should print our table headers
print(records) #should print all our records


# To write data to this file;
my_data = [['11', 'Marena', 'Devigne', 'mdevigne0@nasa.gov', 'Female', '66.176.191.249'], ['12', 'Elsi', 'Betke', 'ebetke1@technorati.com', 'Male', '58.150.90.47']]
my_file = "writeInfo.csv"
with open(my_file,'w', newline="") as file:
    writer = csv.writer(file)
    writer.writerows(my_data)





