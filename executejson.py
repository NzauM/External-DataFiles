import json #import the json package to encode and decode json data

with open("info.json","r") as read_file: #open the json file in read mode
    data = json.load(read_file) #You now have your data as a list.
    print(type(data)) #should return 'list'

for details in data:
    print(details['first_name']) #to get all the first names
    #Try to change Patrizio's name
    if(details['first_name'] == "Patrizio"):
        details['first_name'] = "WE HAVE CHANGED YOUR NAME"
print(details) #should now return the last user, with his first name changed


