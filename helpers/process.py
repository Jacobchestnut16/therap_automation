# helpers/process.py
import pandas as pd
import os
from config import RAW_DATA_PATH, PROCESSED_DATA_PATH, MIN_VALUE, MAX_VALUE

def process_report(file_name):
    file_path = os.path.join(RAW_DATA_PATH, file_name)
    df = pd.read_excel(file_path)

    # Example flagging: check numeric columns for out-of-range values
    flagged = df[(df.select_dtypes(include='number') < MIN_VALUE) |
                 (df.select_dtypes(include='number') > MAX_VALUE)]

    processed_file = os.path.join(PROCESSED_DATA_PATH, f"flagged_{file_name}")
    flagged.to_excel(processed_file, index=False)
    print(f"Processed report saved to {processed_file}")
