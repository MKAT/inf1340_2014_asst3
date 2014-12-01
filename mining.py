#!/usr/bin/env python3

""" Docstring """

__author__ = 'Laurel Robinson, Melissa Tomko, Anne Simon'
__email__ = "laurel.robinson@mail.utoronto.ca, melissa.tomko@mail.utoronto.ca, anne.simon@mail.utoronto.ca"

# imports one per line
import json
import datetime
import math
from operator import itemgetter

stock_data = {}
monthly_averages = {}
year_month_volume = {}
year_month_sales = {}


def read_stock_data(stock_name, stock_file_name):

    """
    Import JSON file and convert into a data structure

    :param stock_name: string
    :param stock_file_name: JSON file
    :return: tuple
    """

    # process stock_name
    try:
        stock_records = read_json_from_file(stock_file_name)
    except FileNotFoundError:
        pass

    for stock_record in stock_records:
       c = stock_record['Close']
       v = stock_record['Volume']
       year_month = stock_record['Date'][0:4] + '/' + stock_record['Date'][5:7]

       if year_month in year_month_sales:
           year_month_sales[year_month].append((v, c))
       else:
           year_month_sales[year_month] = [(v, c)]

    year_month_average_sales = {}
    for ym, year_month_item in year_month_sales.items():
        average_sales = average_price(year_month_item)
        year_month_average_sales[ym] = average_sales

def average_price(vc_list):
    numerator = 0
    denominator = 0
    for v,c in vc_list:
        numerator += (v * c)
        denominator += v

    return (numerator / denominator)


def six_best_months(year_month_average_sales):
    sales_value = {}
    for yrmo, sales in year_month_average_sales.items():
        sales_value[format(sales)] = yrmo

    sorted_sales_value = []
    for sorted_sales in sorted(year_month_average_sales.values()):
        sorted_sales_value.append(sorted_sales)

    six_best_month_sales = {}
    count_six = 0
    for highest_sales in reversed(sorted_sales_value):
        if count_six < 6:
            yearmonth = sales_value[format(highest_sales)]
            six_best_month_sales[yearmonth] = highest_sales
            count_six = count_six + 1
        else:
            break
    return list(six_best_month_sales.items())


def six_worst_months(year_month_average_sales):
    sales_value = {}
    for yrmo, sales in year_month_average_sales.items():
        sales_value[format(sales)] = yrmo

    six_worst_month_sales = {}
    count_six = 0
    sorted_sales_value = []
    for sorted_sales_value in sorted(year_month_average_sales.values()):
        if count_six < 6:
            yearmonth = sales_value[format(sorted_sales_value)]
            six_worst_month_sales[yearmonth] = sorted_sales_value
            count_six = count_six + 1
        else:
            break
    return list(six_worst_month_sales.items())


def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)

#Melissa's attempt at the 'Compare 2 Stocks' Bonus
vc_list = [] #input our tuple to call from-- chose vc_list because it is what we used to compute the averages


# def average_price(vc_list):
#     return sum(vc_list) * 1.0 / len(vc_list)
# avg = average_price(vc_list)
# variance = map(lambda x: (x-avg)**2, vc_list)
#
# average(variance)
# standard_deviation = math.sqrt(average(variance))