from pathlib import Path
import pandas as pd 
import numpy as np
import sys

## Activity 5 
mypkg1_directory = Path(__file__).resolve().parent
src_root1 = mypkg1_directory.parent  
sys.path.append(str(src_root1))
csv_file_path1 = src_root1 / 'data' / 'paralympics_events_raw.csv' 

df_left = pd.read_csv(csv_file_path1)

mypkg2_directory = Path(__file__).resolve().parent
src_root2 = mypkg2_directory.parent  
sys.path.append(str(src_root2))
csv_file_path2 = src_root2 / 'data' / 'npc_codes.csv' 

df_right = pd.read_csv(csv_file_path2, encoding='utf-8', encoding_errors='ignore', usecols=['Code', 'Name'])
df_merged = df_left.merge(df_right, how='left', left_on='country', right_on='Name')

## Activity 7 
df_merged.drop(columns=('Name'), axis=1, inplace=True)
df_cleaned = df_merged.dropna(subset=['participants_m','participants_f'])
missing_values = df_cleaned.isna()

# remember to reset the index 
df_cleaned = df_cleaned.reset_index(drop=True)

## Activity 8
print(df_cleaned['type'].unique())
df_cleaned['type'] = df_cleaned['type'].str.strip()
df_cleaned['type'] = df_cleaned['type'].str.lower()

## Activity 9 
columns_to_convert = ['countries', 'events', 'participants_m', 'participants_f', 'participants']
df_cleaned[columns_to_convert] = df_cleaned[columns_to_convert].astype(int)

df_cleaned['start'] = pd.to_datetime(df_cleaned['start'], dayfirst=True)
df_cleaned['end'] = pd.to_datetime(df_cleaned['end'], dayfirst=True)

df_cleaned['duration'] = (df_cleaned['end'] - df_cleaned['start']).dt.days
print(df_cleaned.dtypes)
print(df_cleaned.duration)

## Activity 10
# 





