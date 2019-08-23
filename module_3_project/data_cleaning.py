"""
This module is for your data cleaning.
It should be repeatable.

## PRECLEANING
There should be a separate script recording how you transformed the json api
calls into a dataframe and csv.

## SUPPORT FUNCTIONS
There can be an unlimited amount of support functions.
Each support function should have an informative name and return the partially
cleaned bit of the dataset.
"""
import pandas as pd
import numpy as np
import api_call as api
import transform_response as t


def response_to_df_csv():
    """
    Calls supporting functions from 'api_call.py' and 'transform_response.py'
    to call api, convert the response to a dataframe, and save the dataframe
    as a .csv file.
    """
    results = api.call_api()
    df = t.get_dataframe(results)
    t.save_csv(df)
    return df


def drop_cols(df, cols=['EMP_S', 'FIRMPDEMP_S', 'GEO_ID', 'GEO_TTL', 'MSA',
                        'PAYANN_S', 'RCPPDEMP_S', 'ST', 'YEAR', 'YIBSZFI',
                        'YIBSZFI_TTL', 'us', 'Unnamed: 0']):
    """
    Drops columns unused in data analysis.
    """
    df = df.drop(columns=cols)
    return df


def lowercase_columns(df):
    """
    Converts column names to lowercase.
    """
    cols = list(df.columns)
    lower_cols = [col.lower() for col in cols]
    df.columns = lower_cols
    return df


def make_numeric(
    df,
    vars_=[
        'emp',
        'empszfi',
        'firmpdemp',
        'payann',
        'rcppdemp',
        'eth_group',
        'geotype',
        'rcpszfi',
        'sex',
        'vet_group']):
    """
    Takes columns with numbers as object datatypes and converts them
    to numeric datatypes. Objects are coerced to type int or type float.
    """
    df[vars_] = df[vars_].apply(pd.to_numeric)
    return df


def drop_zero_pay(df):
    """
    Drops rows where annual pay is reported as zero (volunteers).
    """
    df = df.loc[df.payann > 0]
    return df


def add_log_col(df, vars_=['payann', 'emp', 'rcppdemp']):
    """
    For variables used in statistical analysis, this function adds columns
    corresponding to the natural log of the variables of interest. Adds suffix
    '_log' to distinguish between original values and natural log values.
    """
    for var in vars_:
        log_var = var + '_log'
        df[log_var] = np.log(df[var])
    return df


def full_clean():
    """
    This is the one function called that will run all the support functions.
    Assumption: Your data will be saved in a data folder and named
    "dirty_data.csv"

    :return: cleaned dataset to be passed to hypothesis testing and
    visualization modules.
    """
    response_to_df_csv()
    dirty_data = pd.read_csv("./data/dirty_data.csv")
    cleaned_data = dirty_data
    cleaned_data = drop_cols(cleaned_data)
    cleaned_data = lowercase_columns(cleaned_data)
    cleaned_data = make_numeric(cleaned_data)
    cleaned_data = drop_zero_pay(cleaned_data)
    cleaned_data = add_log_col(cleaned_data)
    cleaned_data.to_csv('./data/cleaned_for_testing.csv')

    return cleaned_data
