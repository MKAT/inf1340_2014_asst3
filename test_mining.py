#!/usr/bin/env python3

""" Docstring """

__author__ = 'Laurel Robinson, Melissa Tomko, Anne Simon'
__email__ = "laurel.robinson@mail.utoronto.ca, melissa.tomko@mail.utoronto.ca, anne.simon@mail.utoronto.ca"

# imports one per line
from mining import *


def test_goog():
    read_stock_data("data/GOOG.json")
    assert six_best_months(read_stock_data("data/GOOG.json")) == [('2007/12', 693.76), ('2007/11', 676.55), ('2007/10', 637.38),
            ('2008/01', 599.42), ('2008/05', 576.29), ('2008/06', 555.34)]


# def six_best_months_goog():
#     assert [('2007/12', 693.76), ('2007/11', 676.55), ('2007/10', 637.38),
#             ('2008/01', 599.42), ('2008/05', 576.29), ('2008/06', 555.34)]
#
#
# def six_worst_months_goog():
#     assert [('2004/09', 116.38), ('2004/10', 164.52), ('2004/11', 177.09), ('2004/12', 181.01),
#             ('2005/03', 181.18), ('2005/01', 192.96)]
#
#
# def test_tse():
#     read_stock_data("data/TSE-SO.json")
#
#
# def six_best_months_tse():
#     assert [('2007/12', 20.98), ('2007/11', 20.89), ('2013/05', 19.96), ('2013/06', 19.94),
#             ('2013/04', 19.65), ('2007/10', 19.11)]
#
#
# def six_worst_months_tse():
#     assert [('2009/03', 1.74), ('2008/11', 2.08), ('2008/12', 2.25), ('2009/02', 2.41),
#         ('2009/04', 2.75), ('2009/01', 3.14)]
