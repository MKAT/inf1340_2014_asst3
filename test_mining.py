#!/usr/bin/env python3

""" Docstring """

__author__ = 'Laurel Robinson, Melissa Tomko, Anne Simon'
__email__ = "laurel.robinson@mail.utoronto.ca, melissa.tomko@mail.utoronto.ca, anne.simon@mail.utoronto.ca"

# imports one per line
from mining import *


def test_goog():
    read_stock_data("GOOG", "data/GOOG.json")

def six_best_months_goog():
    assert [('2007/12', 693.76), ('2007/11', 676.55), ('2007/10', 637.38),
            ('2008/01', 599.42), ('2008/05', 576.29), ('2008/06', 555.34)]

def six_worst_months_goog():
    assert [('2004/09', 116.38), ('2004/10', 164.52), ('2004/11', 177.09), ('2004/12', 181.01),
            ('2005/03', 181.18), ('2005/01', 192.96)]

def test_tse():
    read_stock_data("TSE-SO", "data/TSE-SO.json")

def six_best_months_tse():
    assert [()]

def six_worst_months_tse():
    assert [()]