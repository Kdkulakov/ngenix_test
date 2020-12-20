import os
from shutil import make_archive, unpack_archive

from work_with_xml import read_xml_get_id_level, read_xml_get_id_object
from work_with_csv import create_csv_id_level, set_file_template
import multiprocessing as mp


CURRENT_DIR = os.path.abspath(os.getcwd()) + '/'
INPUT_DIR = os.path.join(CURRENT_DIR, 'xmls/')
descriptors_list = []


def create_archive(filename, dir_name, count_archives):
    if not os.path.exists(CURRENT_DIR + dir_name):
        os.makedirs(CURRENT_DIR + dir_name)

    full_path = os.path.join(CURRENT_DIR + dir_name)
    for i in range(count_archives):
        make_archive(full_path + filename + '_' + str(i+1), 'zip', INPUT_DIR)


def unpacking_archives(fullpath):
    """Function to unpack archives"""
    if os.path.isfile(fullpath):
        name_file = fullpath.replace(CURRENT_DIR + '/zips/', '')
        unpucked_file_dir = CURRENT_DIR + 'unpucked/' + name_file.rsplit('.', 1)[0] + '/'
        unpack_archive(fullpath, unpucked_file_dir)

        xml_files = os.listdir(unpucked_file_dir)
        for xml_file in xml_files:
            xml_file_path = unpucked_file_dir + xml_file
            read_xml_and_create_csv(xml_file_path)


def pool_unpacking(path):
    """Main function to unpack zips asynchronously"""
    my_files = []
    for root, dirs, files in os.walk(CURRENT_DIR + path):
        for i in files:
            if i.endswith(".zip"):
                my_files.append(os.path.join(root, i))
    set_file_template()
    pool = mp.Pool(min(mp.cpu_count(), len(my_files)))  # number of workers
    pool.map(unpacking_archives, my_files,  chunksize=1)
    pool.close()


def read_xml_and_create_csv(xml_file):

    row_level = read_xml_get_id_level(xml_file)
    create_csv_id_level(row_level)

    read_xml_get_id_object(xml_file)
