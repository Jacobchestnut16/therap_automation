# main.py
from helpers import download, process
import os

def main():
    # 1. Download report
    download.download_report()

    # 2. Find latest downloaded file
    latest_file = max([f for f in os.listdir("data/raw/") if f.endswith(".xlsx")],
                      key=lambda x: os.path.getctime(os.path.join("data/raw/", x)))

    # 3. Process report
    process.process_report(latest_file)

if __name__ == "__main__":
    main()
