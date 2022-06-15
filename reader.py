import csv
import os
import sys


class Reader:

    weather_records = []
    weather_attributes = ["PKT", "Max TemperatureC", "Min TemperatureC", "Max Humidity", " Mean Humidity"]

    def read_weather_monthly_record(self, weather_monthly_record_file_path):
        with open(weather_monthly_record_file_path) as weather_monthly_record:
            try:
                weather_daily_records = csv.DictReader(weather_monthly_record)

                for single_day_weather_record in weather_daily_records:
                    try:
                        date = single_day_weather_record['PKT']
                    except KeyError:
                        date = single_day_weather_record['PKST']
                    self.weather_records.append([
                        date,
                        single_day_weather_record['Max TemperatureC'],
                        single_day_weather_record['Min TemperatureC'],
                        single_day_weather_record['Max Humidity'],
                        single_day_weather_record[' Mean Humidity']
                    ])
            except csv.Error as error:
                sys.exit(f"File format not correct! File {weather_monthly_record_file_path}, "
                         f"line {weather_daily_records.line_num}: {error}")

    def read_weather_yearly_record(self, weather_files_directory_path):
        weather_files = os.listdir(weather_files_directory_path)
        for weather_monthly_record in weather_files:
            self.read_weather_monthly_record(f"{weather_files_directory_path}/{weather_monthly_record}")
        return self.weather_attributes, self.weather_records
