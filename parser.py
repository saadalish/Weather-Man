class Parser:

    weather_records = {}
    weather_attributes = {}

    def parsing_weather_attributes(self, header_record):
        for attribute in header_record:
            self.weather_attributes[attribute] = header_record.index(attribute)

    def parsing_records_into_dictionaries(self, records):
        self.parsing_weather_attributes(records[0])
        for record in records[1:]:
            try:
                year, month, day = record[0].split("-")
                year = int(year)
                month = int(month)
            except (Exception,):
                raise IndexError(f"Desired Record not found on line: {records.index(record)}")
            if len(record) < 5:
                raise IndexError(f"Index out of range for record: {records.index(record)}")
            try:
                for index in range(1, 5):
                    record[index] = int(record[index]) if record[index] != '' else None
                if year not in self.weather_records.keys():
                    self.weather_records[year] = {}
                if month not in self.weather_records[year].keys():
                    self.weather_records[year][month] = []
                self.weather_records[year][month].append(record)
            except (Exception,):
                raise ValueError(f"Invalid Literal for Int Type on line {records.index(record)}")

        return self.weather_attributes, self.weather_records
