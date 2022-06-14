class Computations:

    @staticmethod
    def get_weather_attribute_index(weather_attributes_list, attribute):
        return weather_attributes_list[attribute]

    @staticmethod
    def get_month_and_day_from_date(date):
        year, month, day = date.split("-")
        return int(month), int(day)

    @staticmethod
    def find_maximum_temperature_in_year(year, records):
        weather_attributes, records = records
        temperature = Computations.get_weather_attribute_index(weather_attributes, "Max TemperatureC")
        date = Computations.get_weather_attribute_index(weather_attributes, "PKT")
        maximum_temperature = float("-inf")
        maximum_temperature_record_in_year = []
        for month in records[year].keys():
            days = records[year][month]
            maximum_temperature_record_in_month = max(
                days, key=lambda x: x[temperature] if x[temperature] is not None else float('-inf'))
            if maximum_temperature_record_in_month[temperature] > maximum_temperature:
                maximum_temperature = maximum_temperature_record_in_month[temperature]
                maximum_temperature_record_in_year = maximum_temperature_record_in_month
        month, day = Computations.get_month_and_day_from_date(maximum_temperature_record_in_year[date])
        return month, day, maximum_temperature_record_in_year[temperature]

    @staticmethod
    def find_minimum_temperature_in_year(year, records):
        weather_attributes, records = records
        temperature = Computations.get_weather_attribute_index(weather_attributes, "Min TemperatureC")
        date = Computations.get_weather_attribute_index(weather_attributes, "PKT")
        minimum_temperature = float("inf")
        minimum_temperature_record_in_year = []
        for month in records[year].keys():
            days = records[year][month]
            minimum_temperature_record_in_month = min(
                days, key=lambda x: x[temperature] if x[temperature] is not None else float('inf'))
            if minimum_temperature_record_in_month[temperature] < minimum_temperature:
                minimum_temperature = minimum_temperature_record_in_month[temperature]
                minimum_temperature_record_in_year = minimum_temperature_record_in_month
        month, day = Computations.get_month_and_day_from_date(minimum_temperature_record_in_year[date])
        return month, day, minimum_temperature_record_in_year[temperature]

    @staticmethod
    def find_maximum_humidity_in_year(year, records):
        weather_attributes, records = records
        humidity = Computations.get_weather_attribute_index(weather_attributes, "Max Humidity")
        date = Computations.get_weather_attribute_index(weather_attributes, "PKT")
        max_humidity = float("-inf")
        max_humidity_record_in_year = []
        for month in records[year].keys():
            days = records[year][month]
            max_humidity_record_in_month = max(
                days, key=lambda x: x[humidity] if x[humidity] is not None else float('-inf'))
            if max_humidity_record_in_month[humidity] > max_humidity:
                max_humidity = max_humidity_record_in_month[humidity]
                max_humidity_record_in_year = max_humidity_record_in_month
        month, day = Computations.get_month_and_day_from_date(max_humidity_record_in_year[date])
        return month, day, max_humidity_record_in_year[humidity]

    @staticmethod
    def find_average_highest_temperature_in_month(year, month, records):
        weather_attributes, records = records
        temperature = Computations.get_weather_attribute_index(weather_attributes, "Max TemperatureC")
        average_highest_temperature = 0
        no_of_days = len(records[year][month])
        for day in records[year][month]:
            if day[temperature]:
                average_highest_temperature += day[temperature]
        return average_highest_temperature // no_of_days

    @staticmethod
    def find_average_lowest_temperature_in_month(year, month, records):
        weather_attributes, records = records
        temperature = Computations.get_weather_attribute_index(weather_attributes, "Min TemperatureC")
        average_lowest_temperature = 0
        no_of_days = len(records[year][month])
        for day in records[year][month]:
            if day[temperature]:
                average_lowest_temperature += day[temperature]
        return average_lowest_temperature // no_of_days

    @staticmethod
    def find_average_mean_humidity_in_month(year, month, records):
        weather_attributes, records = records
        humidity = Computations.get_weather_attribute_index(weather_attributes, " Mean Humidity")
        average_mean_humidity = 0
        no_of_days = len(records[year][month])
        for day in records[year][month]:
            if day[humidity]:
                average_mean_humidity += day[humidity]
        return average_mean_humidity // no_of_days

    @staticmethod
    def find_maximum_temperature_on_day(year, month, day, records):
        weather_attributes, records = records
        temperature = Computations.get_weather_attribute_index(weather_attributes, "Max TemperatureC")
        return records[year][month][day-1][temperature]

    @staticmethod
    def find_minimum_temperature_on_day(year, month, day, records):
        weather_attributes, records = records
        temperature = Computations.get_weather_attribute_index(weather_attributes, "Min TemperatureC")
        return records[year][month][day-1][temperature]
