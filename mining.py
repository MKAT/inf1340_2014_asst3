#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import datetime

stock_data = []
monthly_averages = []


def init():
    global stock_data
    stock_data = ""


def read_stock_data(stock_name, stock_file_name):
    """
    Import JSON file and convert into a data structure

    :param stock_name: string
    :param stock_file_name: JSON file
    :return: tuple
    """
    try:
        with open(stock_file_name, 'r') as stock_file:
            stock_file_name_data = stock_file.read()
            stock_contents = json.loads(stock_file)
            print(stock_contents)

            total_volume = {}
            total_average = {}
            monthly_averages = {}

    except:
        raise FileNotFoundError

    for line in stock_contents:
        def read_stock_data(stock_name, stock_file_name):
            global monthly_averages
        def var(monthly_averages):
                  monthly_averages = "september",


        #read_json_from_file('goog.json', 'TSE-SO.json'):



    global stock

    next_monthly_averages == "September"

    if choice


def six_best_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def six_worst_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)



"""
Notes:

end of day stock prices will be provided
we have to report the 2 highest averages


v =
volume for days volume
c=
close for days closed

average_price = (V1 ∗ C1 + V2 ∗ C2)/(V1 + V2)

 each month create a tuple with two items
#append the tuple for each month into a list
monthly_averages_list = []   <-- I think this is supposed to be a tuple


Where is the large json file then???

 """