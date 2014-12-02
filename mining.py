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
year_month_average_sales = {}


def read_stock_data(stock_name, stock_file_name):

    """
    Import JSON file and convert into a data structure

    :param stock_name: string
    :param stock_file_name: JSON file
    :return: tuple
    """

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

    for ym, year_month_item in year_month_sales.items():
        average_sales = average_price(year_month_item)
        year_month_average_sales[ym] = round(average_sales, 2)

def average_price(vc_list):
    numerator = 0
    denominator = 0
    for v,c in vc_list:
        numerator += (v * c)
        denominator += v

    return numerator / denominator


def six_best_months():
    global year_month_average_sales
    sales_value = {}
    # get the year/month and its accumulate average sales from the year_month_average_sales dictionary
    for year_and_month, sales in year_month_average_sales.items():
        # use the average sales as the key for the dictionary and the year and month as the value
        sales_value[format(sales)] = year_and_month

    sorted_sales_value = []
    # sort the value of the given year_month_average_sales dictionary. the sorting will be from lowest to highest
    for sorted_sales in sorted(year_month_average_sales.values()):
        # put the sorted average sales into list
        sorted_sales_value.append(sorted_sales)

    six_best_month_sales = {}
    count_six = 0
    # from the sorted_sales_value list, reverse the sorting so that it will be from highest to lowest
    for highest_sales in reversed(sorted_sales_value):
        # get the first 6 records which is equivalent to first 6 months from highest to lowest
        if count_six < 6:
            year_plus_month = sales_value[format(highest_sales)]
            six_best_month_sales[year_plus_month] = highest_sales
            count_six += count_six
        else:
            break # stop the looping if the six highest month sales was already retrieved
    return list(six_best_month_sales.items()) # return the list of six highest sales computed


def six_worst_months(year_month_average_sales):
    sales_value = {}
    for yrmo, sales in year_month_average_sales.items():
        sales_value[format(sales)] = yrmo

    six_worst_month_sales = {}
    count_six = 0
    sorted_sales_value = []

    # this sorted already arranged the average sales from lowest to highest, so just get the first 6 months
    for sorted_sales_value in sorted(year_month_average_sales.values()):
        if count_six < 6:
            yearmonth = sales_value[format(sorted_sales_value)]
            six_worst_month_sales[yearmonth] = sorted_sales_value
            count_six += count_six
        else:
            break
    return list(six_worst_month_sales.items()) # return the list of 6 worst month


def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)
