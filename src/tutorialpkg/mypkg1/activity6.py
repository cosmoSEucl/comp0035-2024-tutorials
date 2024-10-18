from pathlib import Path
import pandas as pd 
import numpy as np
import sys

mypkg1_directory = Path(__file__).resolve().parent
src_root1 = mypkg1_directory.parent  
sys.path.append(str(src_root1))
csv_file_path1 = src_root1 / 'data' / 'paralympics_events_raw.csv' 
df_left = pd.read_csv(csv_file_path1)

df_prepared = df_left.drop(columns=['URL', 'disabilities_included', 'highlights'], axis=1)
print(df_prepared.head)

