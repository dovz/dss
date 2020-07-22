# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu


project_handle = dataiku.api_client().get_project(dataiku.default_project_key())
vars = project_handle.get_variables()
new_val = 'L_PARTKEY,L_LINENUMBER,L_QUANTITY'
vars['standard']['column_list'] = new_val
project_handle.set_variables(vars)

# Recipe inputs
lineitem = dataiku.Dataset("LINEITEM_prepared")
dummy_df = lineitem.get_dataframe()

# Write recipe outputs
dummy = dataiku.Dataset("dummy")
dummy.write_with_schema(dummy_df)
