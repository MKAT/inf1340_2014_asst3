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
y_month_volume = []
y_month_sales = []


def read_stock_data(stock_name, stock_file_name):

    """
    Import JSON file and convert into a data structure

    :param stock_name: string
    :param stock_file_name: JSON file
    :return: tuple
    """

    # process stock_name
    global monthly_averages
    stock_records = read_json_from_file(stock_file_name)
    for stock_record in stock_records:
        closing_price = stock_record['Close']
        day_volume = stock_record['Volume'] # get stock volume
        day_sales = day_volume * closing_price # get stock closing price
        month_sales#Melissa added to refer to green """ as alternate to 3rd if--just uncomment and it will work without red lines
        year_month = stock_record['Date'][0:4] + '/' + stock_record['Date'][5,7] # convert format from yyyy-mm to yyyy/mm
        try:
            if y_month_volume[year_month]:  # check if year and month e.g. 2008/12 already exist in dictionary
                y_month_volume[year_month] = y_month_volume[year_month] + day_volume # add day stock volume into value of year_month
            else:
                y_month_volume[year_month] = day_volume # add day stock volume into value of year_month
            if y_month_sales[year_month]:  # check if year and month e.g. 2008/12 already exist in dictionary
                y_month_sales[year_month] = y_month_sales[year_month] + day_volume # add day volume into value of year month
            else:
                y_month_sales[year_month] = day_sales # add day stock volume into value of year_month
            # the below is to calculate the average price by  (total sales + monthy averages)/volume of sales
            if monthly_averages[year_month]:  # check if year and month e.g. 2008/12 already exist in dictionary
                monthly_averages[year_month]=(y_month_sales[year_month]+[monthly_averages])/y_month_volume[year_month]
            else:
                monthly_averages[year_month] = monthly_averages # add day stock volume into value of year_month

        except:
           raise FileNotFoundError

        y_month_volume[year_month] = day_volume # add day_volume on y_month_volume dictionary
        y_month_sales[year_month] = day_sales
        if month_sales:
            month_sales = monthly_averages[year_month] + day_sales

            """ the except option is giving big issues -- help please """

           #this is the for loop for listing the monthly averages values--not sure if i understand this
    for monthly_averages in year_month:
        year = stock_record['Date'][0:4]
        monthly_averages = monthly_averages[year_month] + year
        month_rank = ord(monthly_averages)[year]
       try:
           monthly_averages:
           monthly_total[year_month] = (y_month_sales[year_month] + [monthly_averages]) / y_month_volume[year_month]



    """
              year_month_volume[year_month] = month_volume # store/replace value of year_month volume with new year_month volume computed
              year_month_sales = [day_sales * month_volume] * 12  #Melissa's attempt at a fix
              month_sales = year_month_sales[year_month] + day_sales # add the day sales with the year_month sales
              year_month_sales[year_month] = month_sales # store/replace value of year_month sales with new year_month sales computed
    """

"""
    # process stock_file_name  - repeat same process made with stock_name
    stock_records = read_json_from_file(stock_file_name)
    for stock_record in stock_records:
       closing_price = stock_record['Close']
       day_volume = stock_record['Volume']
       day_sales = day_volume * closing_price
       year_month = stock_record['Date'][0:4] + '/' + stock_record['Date'][5,7]
       try:
           if year_month_volume[year_month]:
              month_volume = year_month_volume[year_month] + day_volume
              year_month_volume[year_month] = month_volume
              month_sales = year_month_sales[year_month] + day_sales
              year_month_sales = month_sales
       except:
          year_month_volume[year_month] = day_volume
          year_month_sales[year_month] = day_sales






#date month and date year -2 paramenters for a function

                 def date_format (date_string):
                     now = datetime.datetime.now()
                     date = datetime.datetime.striptime(date_string, '%Y-%m-%d')


    except:
        raise FileNotFoundError

    for line in stock_contents:
        def read_stock_data(stock_name, stock_file_name):
            global monthly_averages
        def var(monthly_averages):
                  monthly_averages = "september",


        #read_json_from_file('goog.json', 'TSE-SO.json'):


 def date_month_year ([date_year], [date_month]):
"""


def six_best_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]



def six_worst_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)



# Notes:
#
# end of day stock prices will be provided
# we have to report the 2 highest averages
#
#
# v =
# volume for days volume
# c=
# close for days closed
#
# average_price = (V1 ∗ C1 + V2 ∗ C2)/(V1 + V2)
#
#  each month create a tuple with two items
# #append the tuple for each month into a list
# monthly_averages_list = []   <-- I think this is supposed to be a tuple
#
#
#  """
# #extra notes
# #make the update the year month sales within the try--needs another if loop
#                     # use sales this time
