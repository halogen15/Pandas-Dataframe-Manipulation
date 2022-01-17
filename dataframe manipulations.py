# -*- coding: utf-8 -*-
"""
Dataframe Maniuplation

"""

import pandas as pd

df = pd.DataFrame()


# Keep only the listed columms
df = df[['ID', 'Col1', 'Col2']]


# Rename a column
df_final = df.rename(columns={'Address_x':'Address'})


# Fill null values
df['Some_Indicator'] = df['Some_Indicator'].fillna(0)
df['Some_Indicator'] = df['Some_Indicator'].astype(int)
df['Some_Indicator'] = df['Some_Indicator'].replace({1:'positive', 0: 'negative'})


# Cleaning up combined or merged dataframes by dropping any duplicates
df_final.drop_duplicates(inplace=True)


# Concatenate two dataframes with the same columms
df_combined = pd.concat([df1, df2], ignore_index=True, sort=False)


# Merge two dataframes with a shared key and different columns
df_merged = pd.merge(left=df1, right=df2, on='ID', how='left')


# Create grouped view and count
def group_on_one(df, col_name1):
    #Groupby and list
    group_list=df.groupby([col_name1])['ID'].apply(list).reset_index(name='IDs')
    #Groupby and count
    group_df=df.groupby([col_name1]).agg({'ID':['count']})
    group_df.columns = ['ID_Count']
    group_df = group_df.reset_index()
    #Merge these dataframes together
    group_final = pd.merge(group_df, group_list, how='outer', on=([col_name1]))
    return(group_final)

group_1_final = group_on_one(df, 'Field_to_Group')

#Group on two columns
def group_on_two(df, col_name1, col_name2):
    #Groupby and list
    group_list=df.groupby([col_name1, col_name2])['ID'].apply(list).reset_index(name='IDs')
    #Groupby and count
    group_df=df.groupby([col_name1, col_name2]).agg({'ID':['count']})
    group_df.columns = ['ID_Count']
    group_df = group_df.reset_index()
    #Merge these dataframes together
    group_final = pd.merge(group_df, group_list, how='outer', on=([col_name1, col_name2]))
    return(group_final)

group_2_final = group_on_two(df, 'Field_to_Group', 'Separated_by_Field2')


# Reorder all columns
cols = ['ID', 'Col2', 'Col3', 'Col4']
df_final = df_final[cols]


# Apply method to a dataframe, such as a utility method
df_second['My_Field'] = df_first['My_Field'].apply(utility_methods.my_method)

