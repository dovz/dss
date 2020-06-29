# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
ods_EVENTS = dataiku.Dataset("ODS_EVENTS")
ods_EVENTS_df = ods_EVENTS.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test_df = ods_EVENTS_df # For this sample code, simply copy input to output

print("aaa")
# Write recipe outputs
test = dataiku.Dataset("test")
test.write_with_schema(test_df)
