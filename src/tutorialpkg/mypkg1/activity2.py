from pathlib import Path
import pandas as pd 
import sys

def describe_dataframe(df: pd.DataFrame):
    num_rows, num_columns = df.shape  
    print(f"This is the number of Rows: {num_rows}")
    print(f"This is the number of Columns:\n{num_columns}")
    print(f"This is the: \n{df.head()}")
    print(f"This is the: \n{df.columns}")
    print(f"Data types of the columns \n{df.dtypes}")
    print(f"This is the:\n{df.info()}")
    print(f"This is the: \n{df.describe()}")


try:
    paralympics_datafile_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_events_raw.csv")
except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

if __name__ == '__main__':
    try: 
        mypkg1_directory = Path(__file__).resolve().parent
        src_root = mypkg1_directory.parent  
        sys.path.append(str(src_root))
        excel_file_path = src_root / 'data' / 'paralympics_all_raw.xlsx' 
    except FileNotFoundError as e:
          print("The file was not found error: {e}")
    df = pd.read_excel(excel_file_path)

    describe_dataframe(df)

# this is new and just wanted to check




     
