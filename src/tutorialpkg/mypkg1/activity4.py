from pathlib import Path
import pandas as pd 
import numpy as np
import sys

mypkg1_directory = Path(__file__).resolve().parent
src_root = mypkg1_directory.parent  
sys.path.append(str(src_root))
excel_file_path = src_root / 'data' / 'paralympics_all_raw.xlsx' 

columns_to_convert = ['countries', 'events', 'participants_m', 'participants_f', 'participants']
df = pd.read_excel(excel_file_path)


df[columns_to_convert] = (
    df[columns_to_convert]
    .replace([np.inf, -np.inf], np.nan)  # Step 1: Replace inf with NaN
    .fillna(0)                            # Step 2: Fill NaN with 0
    .astype('int64')                     # Step 3: Convert to int64
)

'''
df = pd.read_excel(excel_file_path)
# Drop the value or replace by 0 
df = df.dropna(subset=['participants_m'])
""" df['participants_m'].fillna(0, inplace=True) """
df['participants_m'] = df['participants_m'].astype('int64')
'''
print(df.dtypes)

