# -*- coding: utf-8 -*-
"""
Writing dataframes to Excel

"""

import pandas as pd
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell


# Create writer and save each dataframe to an Excel sheet

filepath = 'D:/Data/'
outfile = 'Grouped_Analysis.xlsx'
outpath = filepath + outfile

writer = pd.ExcelWriter(outpath, engine='xlsxwriter', datetime_format='dd-mmm-yyyy')

df1.to_excel(writer, sheet_name='1', engine='xlsxwriter', index=False)
df2.to_excel(writer, sheet_name='2', engine='xlsxwriter', index=False)
df3.to_excel(writer, sheet_name='3', engine='xlsxwriter', index=False)

writer.save()



# Create write and save each dataframe to an Excel sheet and specify formatting in Excel
# This example uses both regular and grouped dataframes
# df_yes and df_no are regular dataframes
# multi_yes and multi_no are grouped dataframes

writer = pd.ExcelWriter(outpath, engine='xlsxwriter', datetime_format='dd-mmm-yyyy')

# Create the sheets
multi_yes.to_excel(writer, sheet_name='Yes', engine='xlsxwriter', index=False)
multi_no.to_excel(writer, sheet_name='No', engine='xlsxwriter', index=False)

# Designate worksheets to be formatted
workbook = writer.book
worksheet1 = writer.sheets['Yes']
worksheet2 = writer.sheets['No']

# Format header row (note this only works with regular dataframes, not multi-indexed like here)
header_format = workbook.add_format({'bold':True, 'text_wrap':True, 'valign':'top', 'aligin':'left', 'border':1})

# Write column headers - Note that here the regular dataframe is used to crate the header names and then applied to the grouped dataframe
for col_num, value in enumerate(df_yes.columns.values):
    worksheet1.write(0, col_num, value, header_format)
    
# Set column width in Excel
worksheet1.set_column('A:A', 10)
worksheet1.set_column('B:B', 12)
worksheet1.set_column('C:C', 24)
worksheet1.set_column('D:D', 16)

workseet1.freeze_panes(1,1)

writer.save()





