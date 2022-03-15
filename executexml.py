import xml.dom.minidom #Import module for parsing xml files
import xml.etree.ElementTree as ET #Import module for traversing the xml element tree

def main():
    # Load and parse the xml file using the parse() function
    doc = xml.dom.minidom.parse("info.xml")

     # To get the name of the first child tag
    firstTag = doc.firstChild.tagName
    print("THIS IS THE FIRST ELEMENT TAG")
    print(firstTag) #prints(dataset)


    # parse the xml element tree
    tree = ET.parse("info.xml")
    elementList = []
    
    #Loop through the tree to get all tags
    for elem in tree.iter():
        elementList.append(elem.tag)

    
    #Now set the list of elemnts to remove duplicates
    elementList = list(set(elementList))

    #You now have a list of all the element tags
    print("THESE ARE ALL THE AVAILABLE ELEMENTS:")
    print(elementList)

    #dictionary that will store our records
    data_records = {}

    # use the lement tags to append data to an object
    for elem in tree.getroot():
        for subelem in elem:
            our_data = [(subelem.tag,subelem.text)]
            data_records.update(our_data)
            print(data_records) #prints out all records in our file

    
    #should hold our latest record
    print("THIS IS OUR LATEST RECORD")
    print(data_records)  



if __name__ == "__main__":
    main();
