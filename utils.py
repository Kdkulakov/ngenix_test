import xml.etree.ElementTree as ET
import xml.dom.minidom
import os
import shutil


CURRENT_DIR = os.path.abspath(os.getcwd())


def check_dir(dir_name):
    """Check dir if not exists - create"""
    if not os.path.exists(CURRENT_DIR + '/' + dir_name):
        os.makedirs(CURRENT_DIR + '/' + dir_name)


def pretty_print_xml_given_root(root, output_xml):
    """
    Useful for when you are editing xml data on the fly
    """
    xml_string = xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml()
    xml_string = os.linesep.join([s for s in xml_string.splitlines() if s.strip()])  # remove the weird newline issue
    with open(output_xml, "w") as file_out:
        file_out.write(xml_string)
        file_out.close()


def remove_directory(folder_name):
    """Remove directory"""
    if folder_name:
        path = folder_name
        shutil.rmtree(path)
