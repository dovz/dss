# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import AAA

# Read recipe inputs
lineitem_prepared = dataiku.Dataset("LINEITEM_prepared")
lineitem_prepared_df = lineitem_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test_python_df = lineitem_prepared_df # For this sample code, simply copy input to output
x = AAA.test_function(5)

# Write recipe outputs
test_python = dataiku.Dataset("test_python")

test_python.write_with_schema(test_python_df)

