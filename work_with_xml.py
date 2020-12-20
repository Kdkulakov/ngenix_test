import xml.etree.ElementTree as xml
from xml.etree.ElementTree import parse
import uuid
import random
from utils import pretty_print_xml_given_root
import os

from work_with_csv import create_csv_id_objects

CURRENT_DIR = os.path.abspath(os.getcwd())


def create_xml(filename, count_files, count_objects, dir_name):
    if count_files and count_objects:
        """
        Создаем XML файл.
        """
        for i in range(count_files):

            root = xml.Element("root")
            xml.SubElement(root, "var", name="id", value=str(uuid.uuid4()))

            level = random.randint(1, 100)
            xml.SubElement(root, "var", name="level", value=str(level))

            objects = xml.SubElement(root, "objects")

            for x in range(count_objects):
                xml.SubElement(objects, "object", name=str(uuid.uuid4()))
            file_name = filename + str(i+1) + '.xml'
            pretty_print_xml_given_root(root, CURRENT_DIR + dir_name + file_name)


def read_xml_get_id_level(filename):
    xmldoc = parse(filename)
    var_id = xmldoc.findall('./var[@name="id"]')
    var_level = xmldoc.findall('./var[@name="level"]')
    row = []
    for i in var_id:
        value = i.attrib['value']
        row.append(value)
    for i in var_level:
        value = i.attrib['value']
        row.append(value)

    return row


def read_xml_get_id_object(filename):
    xmldoc = parse(filename)
    var_id = xmldoc.findall('./var[@name="id"]')
    object_items = xmldoc.findall('./objects/object')

    for item in object_items:
        row = []
        for i in var_id:
            value = i.attrib['value']
            row.append(value)

        name = item.attrib['name']
        row.append(name)
        create_csv_id_objects(row)
