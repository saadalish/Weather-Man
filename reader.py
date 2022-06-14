import os


class Reader:

    weathers = []
    header_row = False

    def read_file(self, name):
        with open(name) as day:
            if self.header_row:
                next(day)
            for record in day:
                record = record.split(",")
                record = record[:2] + [record[3]] + record[7:9]
                self.weathers.append(record)
                self.header_row = True

    def read_folder(self, path):
        files = os.listdir(path)
        for file in files:
            self.read_file(f"{path}/{file}")
        return self.weathers
