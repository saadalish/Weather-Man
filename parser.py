class Parser:

    weather_records = {}
    weather_attributes = {}

    def parsing_weather_attributes(self, weather_attributes):
        self.weather_attributes = {attribute: weather_attributes.index(attribute) for attribute in weather_attributes}

    def parsing_weather_records_into_dictionary(self, raw_weather_records):
        weather_attributes, weather_records = raw_weather_records
        self.parsing_weather_attributes(weather_attributes)

        for single_day_record in weather_records:
            if len(single_day_record) < len(self.weather_attributes.keys()):
                raise IndexError(
                    f"Index out of range for this weather record: {single_day_record} "
                    f"expecting {len(self.weather_attributes.keys())} attributes"
                )

            try:
                year, month, day = single_day_record[self.weather_attributes['PKT']].split("-")
                year = int(year)
                month = int(month)
                for index in range(1, len(self.weather_attributes.keys())):
                    single_day_record[index] = int(single_day_record[index]) if single_day_record[index] != '' else None
                if year not in self.weather_records.keys():
                    self.weather_records[year] = {}
                if month not in self.weather_records[year].keys():
                    self.weather_records[year][month] = []
                self.weather_records[year][month].append(single_day_record)
            except ValueError as error:
                print(f"Desired weather attribute not found for this {single_day_record} weather record. "
                      f"Details: {error}")

        return self.weather_attributes, self.weather_records
