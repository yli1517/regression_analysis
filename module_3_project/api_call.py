#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:06:23 2019

@author: marissaeppes

This script takes a base url for the api call, a sting of variables that need
to be included in the call to retrieve complete data, and an end addition to
the url. The functions makes the api call.
"""
import requests

BASE_URL = "http://api.census.gov/data/2014/ase/csa?get="
END_URL = "&for=us:*"
VARS_STR = 'EMP,EMP_S,EMPSZFI,EMPSZFI_TTL,ETH_GROUP,ETH_GROUP_TTL,FIRMPDEMP,\
            FIRMPDEMP_S,GEO_ID,GEO_TTL,GEOTYPE,MSA,NAICS2012,NAICS2012_TTL,\
            PAYANN,PAYANN_S,RACE_GROUP,RACE_GROUP_TTL,RCPPDEMP,RCPPDEMP_S,\
            RCPSZFI,RCPSZFI_TTL,SEX,SEX_TTL,ST,VET_GROUP,VET_GROUP_TTL,YEAR,\
            YIBSZFI,YIBSZFI_TTL'
VARS_STR = VARS_STR.replace(" ", "")


def call_api(base_url=BASE_URL, end_url=END_URL, vars_str=VARS_STR):
    """
    Concatenates base url, string of variables, and url ending, passes complete
    url into api request, returns json object.
    """
    url = base_url + vars_str + end_url
    response = requests.get(url)
    results = response.json()
    return results
