#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:19:32 2019

@author: marissaeppes

This script takes the json generared from api, converts it to a dataframe, and
saves the dataframe as a .csv file.
"""

import pandas as pd


def get_dataframe(api_result):
    """
    Converts json object to dataframe, uses the first element of the json,
    which contains the column headers as the columns of the dataframe, uses
    remaining elements as data.
    """

    df = pd.DataFrame(api_result)
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header

    return df


def save_csv(df):
    """
    Saves dataframe as .csv file.
    """
    df.to_csv(r'data/dirty_data.csv')
