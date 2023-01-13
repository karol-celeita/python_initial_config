
# Firstly we have to import 'xml.etree.ElementTree' for creating a subtree
import xml.etree.ElementTree as ET

users_list = ["GeeksForGeeks", "Arka", "Computer Science", "Engineering", "Portal"]

def create_xml(name_file_xml="default"):
    """_summary_
    """
    try:
        # we make root element
        usrconfig = ET.Element("usrconfig")

        # create sub element
        usrconfig = ET.SubElement(usrconfig, "usrconfig")

        # insert list element into sub elements
        for user in range(len(users_list)):

            usr = ET.SubElement(usrconfig, "usr")
            usr.text = str(users_list[user])

        tree = ET.ElementTree(usrconfig)

        # write the tree into an XML file
        tree.write(f"{name_file_xml}.xml", encoding='utf-8', xml_declaration=True)
        

        
    except NameError as error_name:  
        print(f"NameError: {error_name}")
    
    except Exception as error:
        print(error)
     
create_xml()
