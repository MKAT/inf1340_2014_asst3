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
year_month_volume = []
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
       v = stock_record['Volume'] # get stock volume
       # #day_sales = day_volume * closing_price # get stock closing price
       # #month_sales#Melissa added to refer to green """ as alternate to 3rd if--just uncomment and it will work without red lines
       year_month = stock_record['Date'][0:4] + '/' + stock_record['Date'][5,7] # convert format from yyyy-mm to yyyy/mm

       if year_month in year_month_sales:
           year_month_sales[year_month].append((v, c))
       else:
           year_month_sales[year_month] = [(v, c)]

def average_price(vc_list):
    numerator = 0
    denominator = 0
    for v,c in vc_list:
        numerator += (v * c) # numerator = numerator + (v*c)
        denominator += v

    return (numerator / denominator)

"""



TO DO
iterate through stock records(take a for loop)
google dictionary.items
inside for loop compute tea average price and call the average price function
store that in a new list
find a way to sort the list--make the list look like [('2013/09', 33.2), ('2001/12', 3.2)]
inorder or you to index the 1st 6
list slicing.

make a

"""



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
#extra notes
#make the update the year month sales within the try--needs another if loop
                    # use sales this time