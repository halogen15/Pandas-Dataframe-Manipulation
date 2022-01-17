# -*- coding: utf-8 -*-
"""
Examples of conversions
"""

import pandas as pd

# Convert timestamp to human readable datetime
def fixtime(value):
    try:
        date = (datetime.datetime.utcfromtimestamp(value/1000).isoformat())+"Z"
        return date
    except:
        return value
    
def dateformat(df):
    for i, row in df.iterrows():
        datefixed = fixtime(row['timestamp'])
        df.loc[i, 'timestamp'] = datefixed
    return df

df = dateformat(df)


# Formating date
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
df['Month'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m')
df['Year'] = pd.to_datetime(df['Date']).dt.strftime('%Y')


# Convert value to binary
def fixbinary(value):
    try:
        tmp_val = int(value)
        tmp_val = bin(tmp_val)[2:]
        val = tmp_val.zfill(32)
        return val
    except:
        return value

def binaryformat(df):
    for i, row in df.iterrows():
        binaryfixed = fixbinary(row['binary_field_name'])
        df.loc(i, 'binary_field_name') = binaryfixed
    return df

df = binaryformat(df)


# Extract email
def email_extractor(df, str_col_id, str_col_text, is_lowercase=True, re_email=re.compile(r'([a-zA-Z0-9_.+-\\.\\!\\#\\$\\%\\&\\*\\?\\=\\^\\{\\}\\]+[a-zA-Z0-9-_]+\.[a-zA-z0-9-_\\.]{2,})', flags=re.IGNORECASE)):
    rtn_df = []
    for i, val_row in df.iterrows():
        tmp_id = val_row[str_col_id]
        tmp_email = val_row[str_col_text]
        tmp_strs01 = tmp_email.split(",")
        tmp_strs02 = []
        for i, str_i in enumerate(tmp_strs01):
            tmp_strs02.extend(str_i.split(';'))
        tmp_str03 = []
        for i, str_i in enumerate(tmp_strs02):
            tmp_strs03.extend(str_i.split('/'))
        for i, str_i in enumerate(tmp_strs03):
            tmp_emails = re.findall(re_email, str_i)
            
    rtn_df.append(pd.DataFrame({'Message_ID':[tmp_id]*len(tmp_emails), 'Email_Extracted':tmp_emails}))

    df_final = pd.concat(rtn_df, ignore_index=False, sort=False)
    
    if(is_lowercase==False):
        df_final['Email_Extracted'] = df_final['Email_Extracted'].str.lower()
    
    return(df_final)

df_extracted_emails = email_extractor(df=df_org, str_col_id='ID_Field', str_col_text='Msg_text', is_lowercase=True)



        