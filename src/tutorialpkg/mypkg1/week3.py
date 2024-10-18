from pathlib import Path
import pandas as pd 
import numpy as np
import sys
import matplotlib.pyplot as plt


def draw_sample_plot(df):
    df.plot(title='Sample Plot', xlabel='Time', ylabel='Number of participants')
    plt.show()
    df.boxplot(subplots=True, sharey=False)
    plt.show()


if __name__ == '__main__':
    # Sample DataFrame
    mypkg1_directory = Path(__file__).resolve().parent
    src_root = mypkg1_directory.parent  
    sys.path.append(str(src_root))
    csv_file_path = src_root / 'data' / 'paralympics_events_prepared.csv'
    data_plot = pd.read_csv(csv_file_path, usecols=['participants_m','participants_f'])

    draw_sample_plot(data_plot)



