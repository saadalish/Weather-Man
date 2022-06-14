from Computations import Computations
import calendar


class Report:

    @staticmethod
    def find_maximum_temperature_in_year(year, records):
        month, day, temperature = Computations.find_maximum_temperature_in_year(year, records)
        print("Highest: " + str(temperature) + "C on " + calendar.month_name[month] + " " + str(day))

    @staticmethod
    def find_minimum_temperature_in_year(year, records):
        month, day, temperature = Computations.find_minimum_temperature_in_year(year, records)
        print("Lowest: " + str(temperature) + "C on " + calendar.month_name[month] + " " + str(day))

    @staticmethod
    def find_maximum_humidity_in_year(year, records):
        month, day, humidity = Computations.find_maximum_humidity_in_year(year, records)
        print("Humidity: " + str(humidity) + "% on " + calendar.month_name[month] + " " + str(day))

    @staticmethod
    def find_average_highest_temperature_in_month(year, month, records):
        average = Computations.find_average_highest_temperature_in_month(year, month, records)
        print("Highest Average: " + str(average) + "C")

    @staticmethod
    def find_average_lowest_temperature_in_month(year, month, records):
        average = Computations.find_average_lowest_temperature_in_month(year, month, records)
        print("Lowest Average: " + str(average) + "C")

    @staticmethod
    def find_average_mean_humidity_in_month(year, month, records):
        average = Computations.find_average_mean_humidity_in_month(year, month, records)
        print("Average Mean Humidity: " + str(average) + "%")

    @staticmethod
    def generate_barchart(temp, is_highest):
        if is_highest:
            return "\033[91m {}\033[00m".format("+" * temp)
        return "\033[94m {}\033[00m".format("+" * temp)

    @staticmethod
    def find_maximum_minimum_temperature_on_day(year, month, day, records):
        maximum_temperature = Computations.find_maximum_temperature_on_day(year, month, day, records)
        minimum_temperature = Computations.find_minimum_temperature_on_day(year, month, day, records)
        if maximum_temperature:
            print(str(day) + " " + Report.generate_barchart(maximum_temperature, True) + " " + str(maximum_temperature)
                  + "C")
        if minimum_temperature:
            print(str(day) + " " + Report.generate_barchart(minimum_temperature, False) + " " + str(minimum_temperature)
                  + "C")

    @staticmethod
    def find_maximum_minimum_temperature_on_days_in_month(year, month, records):
        days = records[year][month]
        for day in days:
            Report.find_maximum_minimum_temperature_on_day(year, month, day[2], records)