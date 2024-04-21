import os.path
import xml.etree.ElementTree as ET


# Function that fetches data from file and parses it to an ET.Element
def get_root(file_path):
    if is_xml(file_path):
        if is_xml_not_empty(file_path):
            tree = ET.parse(file_path)
            return tree.getroot()
    else:
        return None


# Function that checks if the file exists and has .xml extension
def is_xml(file_path):
    if os.path.isfile(file_path):
        if file_path.lower().endswith('.xml'):
            return True
    print("File not found! Check if you uploaded correct format of the file.")
    return False


# Function that checks if the .xml file is empty
def is_xml_not_empty(file_path):
    if os.path.getsize(file_path) == 0:
        return False
    return True
