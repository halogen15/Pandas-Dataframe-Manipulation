# -*- coding: utf-8 -*-
"""
Center of geoshapes
Are geoshapes clustered or scattered?

"""

import pandas as pd
from scipy.stats import zscore

# Find the center of a geoshape
def geo_zscore(df):
    location_cols = df[['lon', 'lat']]
    location_cols = location_cols.rename(columns={'lat':'lat_zscore', 'lon':'lon_zscore'})
    #Calculate z-scores for lats and lons of the shape
    location_cols = location_cols.apply(zscore)
    df_geo = pd.concat([df, location_cols], axis=1)
    df_geo = df_geo[['address', 'lat_zscore', 'lon_zscore', 'timestamp']]
    df_geo


# Determine if lat/lon is within a cluster or spread out
def count_center(lst):
    central = 1
    outlier = 1
    for i in lst:
        if abs(i) > 1.15: # 75% or more of the lon/lat have z-score above 1.15 (CI 75%)
            central += 1
        else:
            outlier += 1
    return central, outlier

def geo_centrality(df):
    lon_zscore = df['lon_zscore'].tolist()
    lat_zscore = df['lat_zscore'].tolist()
    lon_center, lon_outlier = count_center(lon_zscore)
    lat_center, lat_outlier = count_center(lat_zscore)
    
    if (lon_center/lon_outlier) >= 0.75:
        clustered = 1
    else:
        clustered = 0
    return clustered

df2 = geo_zscore(df)
my_cluster = geo_centrality(df2)