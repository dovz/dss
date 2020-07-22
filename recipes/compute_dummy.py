# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
lineitem_prepared = dataiku.Dataset("LINEITEM_prepared")
lineitem_prepared_df = lineitem_prepared.get_dataframe()

#set column_list variable
project_handle = dataiku.api_client().get_project(dataiku.default_project_key())
vars = project_handle.get_variables()
new_val = 'L_PARTKEY,L_LINENUMBER,L_QUANTITY'
vars['standard']['column_list'] = new_val
project_handle.set_variables(vars)


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

dummy_df = lineitem_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
dummy = dataiku.Dataset("dummy")
dummy.write_with_schema(dummy_df)
