from pathlib import Path
import csv
from operator import itemgetter


class csv_modifier():

    path = Path(__file__).parent.absolute()
    txt_path = str(path) +'/../static/german/dictionary.txt'
    csv_path = txt_path[:-3] + 'csv'

    def write_csv(self, lines):
        with open(self.csv_path, mode='w') as dict_file:
            word_writer = csv.writer(dict_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for line in lines:
                word_writer.writerow([line[2].lower(), line[3].lower(), line[0].lower()])

    def append_csv(self, row):
        with open(self.csv_path, mode='a') as dict_file:
            writer = csv.writer(dict_file)
            writer.writerow(row)

    def sort_by_col(self, lines):
        # sorted(lines, key=itemgetter(0))
        lines.sort(key=lambda x: x[3].casefold())
        # print(lines[:5])
        self.write_csv(lines)

    # def readtxt(self):
    #     with open(self.txt_path) as f:
    #         content = f.readlines()
    #         lines = []
    #         for line in content:
    #             line = line.strip().split(' ')[1:]
    #             lines.append(line)
    #     return lines

    def read_csv(self):
        content = []
        with open(self.csv_path, mode='r') as dict_file:
            csv_reader = csv.reader(dict_file, delimiter=',')
            for row in csv_reader:
                content.append([row[0], row[1], row[2]])
        return content

    # lines = readtxt(txt_path)

    # write_csv(lines)

    # sort_by_col(lines)

    # read_csv(csv_path)

    # append_csv(['die', ' öffentliche verkehrsmittel', 'public transport'])
# editcsv = csv_editor()
# editcsv.read_csv()