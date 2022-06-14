class Computations:

    @staticmethod
    def find_maximum_temperature_in_year(year, records):
        maximum_temperature = float("-inf")
        maximum_temperature_record = []
        for month in records[year].keys():
            days = records[year][month]
            candidate = max(days, key=lambda x: x[3] if x[3] is not None else float('-inf'))
            if candidate[3] > maximum_temperature:
                maximum_temperature = candidate[3]
                maximum_temperature_record = candidate
        return maximum_temperature_record[1], maximum_temperature_record[2], maximum_temperature_record[3]

    @staticmethod
    def find_minimum_temperature_in_year(year, records):
        minimum_temperature = float("inf")
        minimum_temperature_record = []
        for month in records[year].keys():
            days = records[year][month]
            candidate = min(days, key=lambda x: x[5] if x[5] is not None else float('inf'))
            if candidate[5] < minimum_temperature:
                minimum_temperature = candidate[5]
                minimum_temperature_record = candidate
        return minimum_temperature_record[1], minimum_temperature_record[2], minimum_temperature_record[5]

    @staticmethod
    def find_maximum_humidity_in_year(year, records):
        max_humidity = float("-inf")
        max_humidity_record = []
        for month in records[year].keys():
            days = records[year][month]
            candidate = max(days, key=lambda x: x[9] if x[9] is not None else float('-inf'))
            if candidate[9] > max_humidity:
                max_humidity = candidate[9]
                max_humidity_record = candidate
        return max_humidity_record[1], max_humidity_record[2], max_humidity_record[9]

    @staticmethod
    def find_average_highest_temperature_in_month(year, month, records):
        average_highest_temperature = 0
        no_of_days = len(records[year][month])
        for day in records[year][month]:
            if day[3]:
                average_highest_temperature += day[3]
        return average_highest_temperature // no_of_days

    @staticmethod
    def find_average_lowest_temperature_in_month(year, month, records):
        average_lowest_temperature = 0
        no_of_days = len(records[year][month])
        for day in records[year][month]:
            if day[5]:
                average_lowest_temperature += day[5]
        return average_lowest_temperature // no_of_days

    @staticmethod
    def find_average_mean_humidity_in_month(year, month, records):
        average_mean_humidity = 0
        no_of_days = len(records[year][month])
        for day in records[year][month]:
            if day[10]:
                average_mean_humidity += day[10]
        return average_mean_humidity // no_of_days

    @staticmethod
    def find_maximum_temperature_on_day(year, month, day, records):
        return records[year][month][day-1][3]

    @staticmethod
    def find_minimum_temperature_on_day(year, month, day, records):
        return records[year][month][day-1][5]
