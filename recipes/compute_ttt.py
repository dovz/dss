# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu



# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

ttt_df = ... # Compute a Pandas dataframe to write into ttt


# Write recipe outputs
ttt = dataiku.Dataset("ttt")
ttt.write_with_schema(ttt_df)
