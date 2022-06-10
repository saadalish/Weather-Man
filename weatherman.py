__weather__ = {}  # for storing weather records
__months__ = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct",
              11: "Nov", 12: "Dec"}

import os
import sys


class Parser:

    @staticmethod
    def extracting_info_file_name(file_name):
        city, weather, year, month = file_name.split("_")
        city = city.split("/")[-1]
        month, ext = month.split(".")
        return city, year, month

    def read_file(self, file_name):
        city, year, month = self.extracting_info_file_name(file_name)
        if city not in __weather__.keys():
            __weather__[city] = {}
        if year not in __weather__[city].keys():
            __weather__[city][year] = {}
        if month not in __weather__[city][year].keys():
            __weather__[city][year][month] = {}
        # reading file content
        file = open(file_name, 'r')
        lines = file.readlines()

        for line in range(1, len(lines)):
            info = lines[line].split(",")
            details = {}
            details.update({"PKT": info[0]})
            details.update({"Max TemperatureC": int(info[1]) if info[1] != '' else None})
            details.update({"Mean TemperatureC": int(info[2])if info[2] != '' else None})
            details.update({"Min TemperatureC": int(info[3]) if info[3] != '' else None})
            details.update({"Dew PointC": int(info[4]) if info[4] != '' else None})
            details.update({"MeanDew PointC": int(info[5]) if info[5] != '' else None})
            details.update({"Min DewpointC": int(info[6]) if info[6] != '' else None})
            details.update({"Max Humidity": int(info[7]) if info[7] != '' else None})
            details.update({"Mean Humidity": int(info[8]) if info[8] != '' else None})
            details.update({"Min Humidity": int(info[9]) if info[9] != '' else None})
            details.update({"Max Sea Level PressurehPa": info[10]})
            details.update({"Mean Sea Level PressurehPa": info[11]})
            details.update({"Min Sea Level PressurehPa": info[12]})
            details.update({"Max VisibilityKm": info[13]})
            details.update({"Mean VisibilityKm": info[14]})
            details.update({"Min VisibilitykM": info[15]})
            details.update({"Max Wind SpeedKm/h": info[16]})
            details.update({"Max Gust SpeedKm/h": info[17]})
            details.update({"Precipitationmm": info[18]})
            details.update({"CloudCover": info[19]})
            details.update({"Events": info[20]})
            details.update({"WindDirDegrees": info[21]})
            __weather__[city][year][month][line] = details

    def read_folder(self, directory_path):
        files = os.listdir(directory_path)
        # file format should be city_weather_year_month.txt for proper parsing
        for file in files:
            self.read_file(directory_path+"/"+file)


class Computations:

    @staticmethod
    def maximum_temperature(year):
        maximum_temp_month = "Jan"
        maximum_temp = __weather__["Murree"][year][maximum_temp_month][1]["Max TemperatureC"]
        maximum_temp_day = 1
        for month in __weather__["Murree"][year].keys():
            for day in __weather__["Murree"][year][month].keys():
                if not maximum_temp:
                    maximum_temp = __weather__["Murree"][year][month][day]["Max TemperatureC"]
                if (__weather__["Murree"][year][month][day]["Max TemperatureC"] and __weather__["Murree"][year][month][day]["Max TemperatureC"] >
                        maximum_temp):
                    maximum_temp = __weather__["Murree"][year][month][day]["Max TemperatureC"]
                    maximum_temp_day = day
                    maximum_temp_month = month
        return maximum_temp, maximum_temp_day, maximum_temp_month

    @staticmethod
    def minimum_temperature(year):

        minimum_temp_month = "Jan"
        minimum_temp = __weather__["Murree"][year][minimum_temp_month][1]["Min TemperatureC"]
        minimum_temp_day = 1
        for month in __weather__["Murree"][year].keys():
            for day in __weather__["Murree"][year][month].keys():
                if not minimum_temp:
                    minimum_temp = __weather__["Murree"][year][month][day]["Min TemperatureC"]
                if (__weather__["Murree"][year][month][day]["Min TemperatureC"] and __weather__["Murree"][year][month][day][
                    "Min TemperatureC"] <
                        minimum_temp):
                    minimum_temp = __weather__["Murree"][year][month][day]["Min TemperatureC"]
                    minimum_temp_day = day
                    minimum_temp_month = month
        return minimum_temp, minimum_temp_day, minimum_temp_month

    @staticmethod
    def maximum_humidity(year):
        max_humidity = 0
        max_humidity_month = "Jan"
        max_humidity_day = __weather__["Murree"][year][max_humidity_month][1]
        for month in __weather__["Murree"][year].keys():
            for day in __weather__["Murree"][year][month].keys():
                if (__weather__["Murree"][year][month][day]["Max Humidity"] and __weather__["Murree"][year][month][day][
                    "Max Humidity"] >
                        max_humidity):
                    max_humidity = __weather__["Murree"][year][month][day]["Max Humidity"]
                    max_humidity_month = month
                    max_humidity_day = day
        return max_humidity, max_humidity_month, max_humidity_day

    @staticmethod
    def average_highest_temperature(year, month):
        average_highest_temp = 0
        no_of_months = len(__weather__["Murree"][year][month].keys())
        for day in __weather__["Murree"][year][month].keys():
            average_highest_temp += __weather__["Murree"][year][month][day]["Max TemperatureC"]
        return average_highest_temp//no_of_months

    @staticmethod
    def average_lowest_temperature(year, month):
        average_lowest_temp = 0
        no_of_months = len(__weather__["Murree"][year][month].keys())
        for day in __weather__["Murree"][year][month].keys():
            average_lowest_temp += __weather__["Murree"][year][month][day]["Min TemperatureC"]
        return average_lowest_temp//no_of_months

    @staticmethod
    def average_mean_humidity(year, month):
        avg_mean_humidity = 0
        no_of_months = len(__weather__["Murree"][year][month].keys())
        for day in __weather__["Murree"][year][month].keys():
            avg_mean_humidity += __weather__["Murree"][year][month][day]["Mean Humidity"]
        return avg_mean_humidity//no_of_months

    @staticmethod
    def maximum_temperature_on_day(year, month, day):
        return __weather__["Murree"][year][month][day]["Max TemperatureC"]

    @staticmethod
    def minimum_temperature_on_day(year, month, day):
        return __weather__["Murree"][year][month][day]["Min TemperatureC"]


class Report:

    @staticmethod
    def maximum_temperature(year):
        temperature, day, month = Computations.maximum_temperature(year)
        print("Highest: " + str(temperature) + "C on " + str(month) + " " + str(day))

    @staticmethod
    def minimum_temperature(year):
        temperature, day, month = Computations.minimum_temperature(year)
        print("Lowest: " + str(temperature) + "C on " + str(month) + " " + str(day))

    @staticmethod
    def maximum_humidity(year):
        humidity, month, day = Computations.maximum_humidity(year)
        print("Humidity: " + str(humidity) + "% on " + str(month) + " " + str(day))

    @staticmethod
    def average_highest_temperature(year, month):
        average = Computations.average_highest_temperature(year, month)
        print("Highest Average: " + str(average) + "C")

    @staticmethod
    def average_lowest_temperature(year, month):
        average = Computations.average_lowest_temperature(year, month)
        print("Average Mean Humidity: " + str(average) + "%")

    @staticmethod
    def average_mean_humidity(year, month):
        average = Computations.average_mean_humidity(year, month)
        print("Lowest Average: " + str(average) + "C")

    @staticmethod
    def generate_barchart(temp, is_highest):
        if is_highest:
            return "\033[91m {}\033[00m".format("+" * temp)
        return "\033[94m {}\033[00m".format("+" * temp)

    @staticmethod
    def maxmin_temperature_on_days(year, month):
        for day in __weather__["Murree"][year][month]:
            temp = Computations.maximum_temperature_on_day(year, month, day)
            temp_ = Computations.minimum_temperature_on_day(year, month, day)
            if temp:
                print(str(day) + " " + Report.generate_barchart(temp, True) + " " + str(temp) + "C")
            if temp_:
                print(str(day) + " " + Report.generate_barchart(temp_, False) + " " + str(temp_) + "C")

    @staticmethod
    def maxmin_temperature_on_days_bonus(year, month):
        for day in __weather__["Murree"][year][month]:
            temp = Computations.maximum_temperature_on_day(year, month, day)
            temp_ = Computations.minimum_temperature_on_day(year, month, day)
            if temp and temp_:
                print(str(day) + " " + Report.generate_barchart(temp_, False) + Report.generate_barchart(temp, True)
                      + " " + str(temp_) + "C" + " " + str(temp) + "C")
            elif temp:
                print(str(day) + " " + Report.generate_barchart(temp, True) + " " + str(temp) + "C")
            elif temp_:
                print(str(day) + " " + Report.generate_barchart(temp_, False) + " " + str(temp_) + "C")


if __name__ == '__main__':
    # Command Line Arguments
    # first: path of weather-files, if weather-files are in the same directory of python file just type None
    # second: operation (-e, -a, -c)
    # third: argument : year, month etc
    if len(sys.argv) < 4:
        print("Less no of Arguments")
    else:
        parser = Parser()
        if sys.argv[1] != "None":
            print(sys.argv[1])
            parser.read_folder(sys.argv[1])
        else:
            parser.read_folder('./weatherfiles')
        arguments = len(sys.argv) - 2
        index = 2
        while arguments > 0:
            if sys.argv[index] == "-e":
                year_ = sys.argv[index+1]
                Report.maximum_temperature(year_)
                Report.minimum_temperature(year_)
                Report.maximum_humidity(year_)
            elif sys.argv[index] == "-a":
                year_, month_ = sys.argv[index+1].split("/")
                month_ = __months__[int(month_)]
                Report.average_highest_temperature(year_, month_)
                Report.average_lowest_temperature(year_, month_)
                Report.average_mean_humidity(year_, month_)
            elif sys.argv[index] == "-c":
                year_, month_ = sys.argv[index + 1].split("/")
                month_ = __months__[int(month_)]
                Report.maxmin_temperature_on_days(year_, month_)
                # for bonus task uncomment the below line
                # Report.maxmin_temperature_on_days_bonus(year_, month_)
            print("")
            arguments -= 2
            index += 2

