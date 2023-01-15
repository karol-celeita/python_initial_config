from constants import DEFAULT_NAME_FILE
from utils import get_timestamp_for_logs as log_time

# Firstly we have to import 'xml.etree.ElementTree' for creating a subtree
import xml.etree.ElementTree as ET
import logging 

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
log = logging.getLogger(__name__)

users_list = ["GeeksForGeeks", "Arka", "Computer Science", "Engineering", "Portal"]

def create_xml(name_file_xml=DEFAULT_NAME_FILE):
    """_summary_

    Args:
        name_file_xml (str, optional): _description_. Defaults to "default".
    """
    log.info(f"{log_time()}  Inicializando conversión a xml...")
             
    try:
        # we make root element
        usrconfig = ET.Element("usrconfig")

        # create sub element
        usrconfig = ET.SubElement(usrconfig, "usrconfig")

        # insert list element into sub elements
        for user in range(len(users_list)):
            valor_lista = str(users_list[user])
            log.info(f"{log_time()}  Iniciando inserción de elemento usr de la lista: {valor_lista}")
            
            usr = ET.SubElement(usrconfig, "usr")
            
            usr.text = valor_lista
            
            log.info(f"{log_time()}  Insertado con exito: {usr.text}")

        tree = ET.ElementTree(usrconfig)

        # write the tree into an XML file
        tree.write(f"{name_file_xml}.xml", encoding='utf-8', xml_declaration=True)
        log.info(f"{log_time()} Archivo convertido exitosamente")
       
        
    except NameError as error_name:  
        log.error(f"{log_time()}  NameError: {error_name}")
    
    except Exception as error:
        log.error(f"{log_time()}  Error Desconocido: {error}")


create_xml()
