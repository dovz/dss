# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku


project_handle = dataiku.api_client().get_project(dataiku.default_project_key())
vars = project_handle.get_variables()
new_val = 'L_PARTKEY,L_LINENUMBER,L_QUANTITY'
vars['standard']['column_list'] = new_val
project_handle.set_variables(vars)
