import argparse
import os

from reader import Reader
from report import Report
from parser import Parser


def validate_directory_path(directory_path):
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(directory_path)
    return directory_path


def extract_year_and_month_from_argument(args):
    extracted_year = None
    extracted_month = None
    try:
        extracted_year, extracted_month = args.split("/")
        extracted_year = int(extracted_year)
        extracted_month = int(extracted_month)
    except ValueError:
        print(f"Invalid Input: {args}")
    finally:
        return extracted_year, extracted_month


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', dest='a', type=str, help='monthly operation')
    parser.add_argument('-e', dest='e', type=int, help='yearly operation')
    parser.add_argument('-c', dest='c', type=str, help='monthly operation | generating reports')
    parser.add_argument('directory', action='store')
    arguments = parser.parse_args()
    weather_files_directory_path = validate_directory_path(arguments.directory)
    reader = Reader()
    parser = Parser()
    raw_weather_records = reader.read_weather_yearly_record(weather_files_directory_path)
    parsed_weather_records = parser.parsing_weather_records_into_dictionary(raw_weather_records)
    if arguments.e:
        Report.generate_report_for_maximum_temperature_in_year(arguments.e, parsed_weather_records)
        Report.generate_report_for_minimum_temperature_in_year(arguments.e, parsed_weather_records)
        Report.generate_report_for_maximum_humidity_in_year(arguments.e, parsed_weather_records)
        print("\n")
    if arguments.a:
        year, month = extract_year_and_month_from_argument(arguments.a)
        Report.generate_report_for_average_highest_temperature_in_month(year, month, parsed_weather_records)
        Report.generate_report_for_average_lowest_temperature_in_month(year, month, parsed_weather_records)
        Report.generate_report_for_average_mean_humidity_in_month(year, month, parsed_weather_records)
        print("\n")
    if arguments.c:
        year, month = extract_year_and_month_from_argument(arguments.c)
        Report.generate_report_for_maximum_minimum_temperature_on_days_in_month(year, month, parsed_weather_records)
        print("\n")
