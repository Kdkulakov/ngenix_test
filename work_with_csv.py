import csv


def create_csv_id_level(row):
    with open('id_level.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)
        file.close()


def create_csv_id_objects(row):
    with open('id_objects.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)
        file.close()


def set_file_template():
    with open('id_level.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "level"])
        file.close()

    with open('id_objects.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "objects"])
        file.close()
