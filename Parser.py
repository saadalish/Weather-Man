class Parser:

    parsed_records = {}

    def record_parsing(self, data):
        for record in data:
            try:
                year, month, day = record[0].split("-")
                year = int(year)
                month = int(month)
                day = int(day)
                for i in range(1, 10):
                    record[i] = int(record[i]) if record[i] != '' else None
                record.pop(0)
                record.insert(0, day)
                record.insert(0, month)
                record.insert(0, year)
                if year not in self.parsed_records.keys():
                    self.parsed_records[year] = {}
                if month not in self.parsed_records[year].keys():
                    self.parsed_records[year][month] = []
                self.parsed_records[year][month].append(record)
            except (Exception,):
                pass

        return self.parsed_records
