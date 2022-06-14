from Report import Report
from Reader import Reader
from Parser import Parser
import argparse
import os


def directory_path(path):
    print(path)
    if os.path.isdir(path):
        return path
    else:
        raise NotADirectoryError(path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', dest='a', type=str, help='monthly operation')
    parser.add_argument('-e', dest='e', type=int, help='yearly operation')
    parser.add_argument('-c', dest='c', type=str, help='monthly operation | generating reports')
    parser.add_argument('directory', nargs='+', action='store')
    args = parser.parse_args()
    directory = directory_path(args.directory[0])
    reader = Reader()
    data = reader.read_folder(directory)
    parser = Parser()
    data = parser.record_parsing(data)
    report = Report()
    if args.e:
        report.find_maximum_temperature_in_year(args.e, data)
        report.find_minimum_temperature_in_year(args.e, data)
        report.find_maximum_humidity_in_year(args.e, data)
        print("\n")
    if args.a:
        year, month = args.a.split("/")
        year = int(year)
        month = int(month)
        report.find_average_highest_temperature_in_month(year, month, data)
        report.find_average_lowest_temperature_in_month(year, month, data)
        report.find_average_mean_humidity_in_month(year, month, data)
        print("\n")
    if args.c:
        year, month = args.a.split("/")
        year = int(year)
        month = int(month)
        report.find_maximum_minimum_temperature_on_days_in_month(year, month, data)
        print("\n")
