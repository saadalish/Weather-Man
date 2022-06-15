import calendar

from computations import Computations


class Report:

    @staticmethod
    def generate_report_for_maximum_temperature_in_year(year, all_weather_records):
        maximum_temperature_month, maximum_temperature_day, maximum_temperature = (
            Computations.find_maximum_temperature_in_year(year, all_weather_records)
        )
        print(f"Highest: {maximum_temperature}C on {calendar.month_name[maximum_temperature_month]} "
              f"{maximum_temperature_day}")

    @staticmethod
    def generate_report_for_minimum_temperature_in_year(year, all_weather_records):
        minimum_temperature_month, minimum_temperature_day, minimum_temperature = (
            Computations.find_minimum_temperature_in_year(year, all_weather_records)
        )
        print(f"Lowest: {minimum_temperature}C on {calendar.month_name[minimum_temperature_month]} "
              f"{minimum_temperature_day}")

    @staticmethod
    def generate_report_for_maximum_humidity_in_year(year, all_weather_records):
        maximum_humidity_month, maximum_humidity_day, maximum_humidity = (
            Computations.find_maximum_humidity_in_year(year, all_weather_records)
        )
        print(f"Humidity: {maximum_humidity}% on {calendar.month_name[maximum_humidity_month]} {maximum_humidity_day}")

    @staticmethod
    def generate_report_for_average_highest_temperature_in_month(year, month, all_weather_records):
        average_highest_temperature_in_month = (
            Computations.find_average_highest_temperature_in_month(year, month, all_weather_records)
        )
        print(f"Highest Average: {average_highest_temperature_in_month}C")

    @staticmethod
    def generate_report_for_average_lowest_temperature_in_month(year, month, all_weather_records):
        average_lowest_temperature_in_month = (
            Computations.find_average_lowest_temperature_in_month(year, month, all_weather_records)
        )
        print(f"Lowest Average: {average_lowest_temperature_in_month}C")

    @staticmethod
    def generate_report_for_average_mean_humidity_in_month(year, month, all_weather_records):
        average_mean_humidity_in_month = (
            Computations.find_average_mean_humidity_in_month(year, month, all_weather_records)
        )
        print(f"Average Mean Humidity: {average_mean_humidity_in_month}%")

    @staticmethod
    def generate_barchart(temperature, is_maximum_temperature):
        return (
            "\033[91m {}\033[00m".format("+" * temperature)
            if is_maximum_temperature
            else "\033[94m {}\033[00m".format("+" * temperature)
        )

    @staticmethod
    def generate_report_for_maximum_minimum_temperature_on_day(year, month, day, all_weather_records):
        maximum_temperature = Computations.find_maximum_temperature_on_day(year, month, day, all_weather_records)
        minimum_temperature = Computations.find_minimum_temperature_on_day(year, month, day, all_weather_records)
        if maximum_temperature:
            print(f"{day+1} {Report.generate_barchart(maximum_temperature, True)} {maximum_temperature}C")
        if minimum_temperature:
            print(f"{day+1} {Report.generate_barchart(minimum_temperature, False)} {minimum_temperature}C")

    @staticmethod
    def generate_report_for_maximum_minimum_temperature_on_days_in_month(year, month, all_weather_records):
        weather_attributes, weather_records = all_weather_records
        weather_daily_records = []
        try:
            weather_daily_records = weather_records[year][month]
        except KeyError:
            print(f"Weather Record not exist for {year} {calendar.month_name[month]}")
        for single_day_record in range(len(weather_daily_records)):
            Report.generate_report_for_maximum_minimum_temperature_on_day(
                year, month, single_day_record, all_weather_records
            )
