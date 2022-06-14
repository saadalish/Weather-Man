import calendar

from computations import Computations


class Report:

    @staticmethod
    def generate_report_for_maximum_temperature_in_year(year, records):
        month, day, temperature = Computations.find_maximum_temperature_in_year(year, records)
        print(f"Highest: {temperature}C on {calendar.month_name[month]}  {day}")

    @staticmethod
    def generate_report_for_minimum_temperature_in_year(year, records):
        month, day, temperature = Computations.find_minimum_temperature_in_year(year, records)
        print(f"Lowest: {temperature}C on {calendar.month_name[month]} {day}")

    @staticmethod
    def generate_report_for_maximum_humidity_in_year(year, records):
        month, day, humidity = Computations.find_maximum_humidity_in_year(year, records)
        print(f"Humidity: {humidity}% on {calendar.month_name[month]} {day}")

    @staticmethod
    def generate_report_for_average_highest_temperature_in_month(year, month, records):
        average = Computations.find_average_highest_temperature_in_month(year, month, records)
        print(f"Highest Average: {average}C")

    @staticmethod
    def generate_report_for_average_lowest_temperature_in_month(year, month, records):
        average = Computations.find_average_lowest_temperature_in_month(year, month, records)
        print(f"Lowest Average: {average}C")

    @staticmethod
    def generate_report_for_average_mean_humidity_in_month(year, month, records):
        average = Computations.find_average_mean_humidity_in_month(year, month, records)
        print(f"Average Mean Humidity: {average}%")

    @staticmethod
    def generate_barchart(temp, is_maximum):
        if is_maximum:
            return "\033[91m {}\033[00m".format("+" * temp)
        return "\033[94m {}\033[00m".format("+" * temp)

    @staticmethod
    def generate_report_for_maximum_minimum_temperature_on_day(year, month, day, records):
        maximum_temperature = Computations.find_maximum_temperature_on_day(year, month, day, records)
        minimum_temperature = Computations.find_minimum_temperature_on_day(year, month, day, records)
        if maximum_temperature:
            print(f"{day} {Report.generate_barchart(maximum_temperature, True)} {maximum_temperature}C")
        if minimum_temperature:
            print(f"{day} {Report.generate_barchart(minimum_temperature, False)} {minimum_temperature}C")

    @staticmethod
    def generate_report_for_maximum_minimum_temperature_on_days_in_month(year, month, records):
        weather_attributes, weather_records = records
        days = weather_records[year][month]
        for day in range(1, len(days)+1):
            Report.generate_report_for_maximum_minimum_temperature_on_day(year, month, day, records)
