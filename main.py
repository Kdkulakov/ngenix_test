from work_with_zip import create_archive, pool_unpacking
from work_with_xml import create_xml
from utils import check_dir
import time

start_time = time.time()
COUNT_ARCHIVES = 50
COUNT_XML_FILES = 100
COUNT_OBJECTS = 10
ZIPS_DIR_NAME = '/zips/'
XMLS_DIR_NAME = '/xmls/'


if __name__ == '__main__':
    print('Step 1: create xmls...')
    check_dir(XMLS_DIR_NAME)
    create_xml('data_file', COUNT_XML_FILES, COUNT_OBJECTS, XMLS_DIR_NAME)

    print('Step 2: create archives...')
    create_archive('/arch', ZIPS_DIR_NAME, COUNT_ARCHIVES)

    print('Step 3: unpacking archives and cooking csv.')
    pool_unpacking(ZIPS_DIR_NAME)

    print(f'Done. time = {time.time() - start_time}')
