import argparse
import os

from reader import Reader
from report import Report
from parser import Parser


def validate_directory_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise NotADirectoryError(path)


def extract_year_and_month_from_argument(arguments):
    return int(arguments.split("/")[0]), int(arguments.split("/")[1])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', dest='a', type=str, help='monthly operation')
    parser.add_argument('-e', dest='e', type=int, help='yearly operation')
    parser.add_argument('-c', dest='c', type=str, help='monthly operation | generating reports')
    parser.add_argument('directory', nargs='+', action='store')
    args = parser.parse_args()
    directory = validate_directory_path(args.directory[0])
    reader = Reader()
    data = reader.read_folder(directory)
    parser = Parser()
    data = parser.parsing_records_into_dictionaries(data)
    report = Report()
    if args.e:
        report.generate_report_for_maximum_temperature_in_year(args.e, data)
        report.generate_report_for_minimum_temperature_in_year(args.e, data)
        report.generate_report_for_maximum_humidity_in_year(args.e, data)
        print("\n")
    if args.a:
        year, month = extract_year_and_month_from_argument(args.a)
        report.generate_report_for_average_highest_temperature_in_month(year, month, data)
        report.generate_report_for_average_lowest_temperature_in_month(year, month, data)
        report.generate_report_for_average_mean_humidity_in_month(year, month, data)
        print("\n")
    if args.c:
        year, month = extract_year_and_month_from_argument(args.c)
        report.generate_report_for_maximum_minimum_temperature_on_days_in_month(year, month, data)
        print("\n")
