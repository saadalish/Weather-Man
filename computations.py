import calendar
import sys


class Computations:

    @staticmethod
    def get_weather_attribute_index(weather_attributes_list, attribute):
        return weather_attributes_list[attribute]

    @staticmethod
    def get_month_and_day_from_date(date):
        year, month, day = date.split("-")
        return int(month), int(day)

    @staticmethod
    def find_maximum_temperature_in_year(year, all_weather_records):
        weather_attributes, weather_records = all_weather_records
        maximum_temperature = Computations.get_weather_attribute_index(weather_attributes, "Max TemperatureC")
        single_day_weather_record_date = Computations.get_weather_attribute_index(weather_attributes, "PKT")
        maximum_temperature_in_year = float("-inf")
        maximum_temperature_record_in_year = []

        try:
            for weather_monthly_records in weather_records[year].keys():
                weather_daily_records = weather_records[year][weather_monthly_records]
                maximum_temperature_record_in_month = max(
                    weather_daily_records, key=lambda x: x[maximum_temperature]
                    if x[maximum_temperature] is not None else float('-inf'))

                if maximum_temperature_record_in_month[maximum_temperature] > maximum_temperature_in_year:
                    maximum_temperature_in_year = maximum_temperature_record_in_month[maximum_temperature]
                    maximum_temperature_record_in_year = maximum_temperature_record_in_month

        except KeyError:
            sys.exit(f"Weather Record not exist for year: {year}")

        finally:
            maximum_temperature_month, maximum_temperature_day = Computations.get_month_and_day_from_date(
                maximum_temperature_record_in_year[single_day_weather_record_date]
            )
            return maximum_temperature_month, maximum_temperature_day, maximum_temperature_in_year

    @staticmethod
    def find_minimum_temperature_in_year(year, all_weather_records):
        weather_attributes, weather_records = all_weather_records
        minimum_temperature = Computations.get_weather_attribute_index(weather_attributes, "Min TemperatureC")
        single_day_weather_record_date = Computations.get_weather_attribute_index(weather_attributes, "PKT")
        minimum_temperature_in_year = float("inf")
        minimum_temperature_record_in_year = []

        try:
            for weather_monthly_records in weather_records[year].keys():
                weather_daily_records = weather_records[year][weather_monthly_records]
                minimum_temperature_record_in_month = min(
                    weather_daily_records, key=lambda x: x[minimum_temperature]
                    if x[minimum_temperature] is not None else float('inf'))

                if minimum_temperature_record_in_month[minimum_temperature] < minimum_temperature_in_year:
                    minimum_temperature_in_year = minimum_temperature_record_in_month[minimum_temperature]
                    minimum_temperature_record_in_year = minimum_temperature_record_in_month

        except KeyError:
            sys.exit(f"Weather Record not exist for year: {year}")

        finally:
            minimum_temperature_month, minimum_temperature_day = Computations.get_month_and_day_from_date(
                minimum_temperature_record_in_year[single_day_weather_record_date]
            )
            return minimum_temperature_month, minimum_temperature_day, minimum_temperature_in_year

    @staticmethod
    def find_maximum_humidity_in_year(year, all_weather_records):
        weather_attributes, weather_records = all_weather_records
        maximum_humidity = Computations.get_weather_attribute_index(weather_attributes, "Max Humidity")
        single_day_weather_record_date = Computations.get_weather_attribute_index(weather_attributes, "PKT")
        max_humidity_in_year = float("-inf")
        max_humidity_record_in_year = []

        try:
            for weather_monthly_records in weather_records[year].keys():
                weather_daily_records = weather_records[year][weather_monthly_records]
                max_humidity_record_in_month = max(
                    weather_daily_records, key=lambda x: x[maximum_humidity]
                    if x[maximum_humidity] is not None else float('-inf'))

                if max_humidity_record_in_month[maximum_humidity] > max_humidity_in_year:
                    max_humidity_in_year = max_humidity_record_in_month[maximum_humidity]
                    max_humidity_record_in_year = max_humidity_record_in_month

        except KeyError:
            sys.exit(f"Weather Record not exist for year: {year}")

        finally:
            max_humidity_month, max_humidity_day = Computations.get_month_and_day_from_date(
                max_humidity_record_in_year[single_day_weather_record_date]
            )
            return max_humidity_month, max_humidity_day, max_humidity_in_year

    @staticmethod
    def find_average_highest_temperature_in_month(year, month, all_weather_records):
        weather_attributes, weather_records = all_weather_records
        maximum_temperature = Computations.get_weather_attribute_index(weather_attributes, "Max TemperatureC")
        average_highest_temperature_in_month = 0

        try:
            for single_day_record in weather_records[year][month]:

                if single_day_record[maximum_temperature]:
                    average_highest_temperature_in_month += single_day_record[maximum_temperature]
                average_highest_temperature_in_month = average_highest_temperature_in_month // len(weather_records[year][month])
        except KeyError:
            sys.exit(f"Weather Record not exist for {year} {calendar.month_name[month]}")

        finally:
            return average_highest_temperature_in_month

    @staticmethod
    def find_average_lowest_temperature_in_month(year, month, all_weather_records):
        weather_attributes, weather_records = all_weather_records
        minimum_temperature = Computations.get_weather_attribute_index(weather_attributes, "Min TemperatureC")
        average_lowest_temperature_in_month = 0

        try:
            for single_day_record in weather_records[year][month]:

                if single_day_record[minimum_temperature]:
                    average_lowest_temperature_in_month += single_day_record[minimum_temperature]
                average_lowest_temperature_in_month = (average_lowest_temperature_in_month
                                                       // len(weather_records[year][month]))
        except KeyError:
            sys.exit(f"Weather Record not exist for {year} {calendar.month_name[month]}")

        finally:
            return average_lowest_temperature_in_month

    @staticmethod
    def find_average_mean_humidity_in_month(year, month, all_weather_records):
        weather_attributes, weather_records = all_weather_records
        mean_humidity = Computations.get_weather_attribute_index(weather_attributes, " Mean Humidity")
        average_mean_humidity_in_year = 0

        try:
            for single_day_record in weather_records[year][month]:

                if single_day_record[mean_humidity]:
                    average_mean_humidity_in_year += single_day_record[mean_humidity]
                average_mean_humidity_in_year = average_mean_humidity_in_year // len(weather_records[year][month])
        except KeyError:
            sys.exit(f"Weather Record not exist for {year} {calendar.month_name[month]}")

        finally:
            return average_mean_humidity_in_year

    @staticmethod
    def find_maximum_temperature_on_day(year, month, day, all_weather_records):
        weather_attributes, weather_records = all_weather_records
        maximum_temperature = Computations.get_weather_attribute_index(weather_attributes, "Max TemperatureC")

        try:
            weather_records[year][month][day][maximum_temperature]
        except KeyError:
            sys.exit(f"Weather Record not exist for {year} {calendar.month_name[month]} {day}")
        finally:
            return weather_records[year][month][day][maximum_temperature]

    @staticmethod
    def find_minimum_temperature_on_day(year, month, day, all_weather_records):
        weather_attributes, weather_records = all_weather_records
        minimum_temperature = Computations.get_weather_attribute_index(weather_attributes, "Min TemperatureC")

        try:
            weather_records[year][month][day][minimum_temperature]
        except KeyError:
            sys.exit(f"Weather Record not exist for {year} {calendar.month_name[month]} {day}")
        finally:
            return weather_records[year][month][day][minimum_temperature]
