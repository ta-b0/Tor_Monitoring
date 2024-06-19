import argparse
import schedule
import time
import os
import subprocess
from datetime import datetime

def download_site(url, base_directory):
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    sub_directory = os.path.join(base_directory, current_time)
    
    os.makedirs(sub_directory, exist_ok=True)

    command = f'torsocks wget -rkp -l 1 {url} -P {sub_directory}'
    try:
        subprocess.check_call(command, shell=True)
        print(f"Downloaded content from {url} and saved to {sub_directory}")
    except subprocess.CalledProcessError:
        print(f"Failed to download content from {url}")
        if os.path.exists(sub_directory):
            os.rmdir(sub_directory)

def job(url, base_directory):
    download_site(url, base_directory)

def main():
    parser = argparse.ArgumentParser(description="Automatic downloader using torsocks and wget")
    parser.add_argument('-u', '--url', type=str, required=True, help='URL to download')
    parser.add_argument('-m', '--minute', type=int, required=True, help='Minute of the hour to run the download job')

    args = parser.parse_args()

    url = args.url
    minute = args.minute
    base_directory = datetime.now().strftime("%Y%m%d")

    schedule.every().hour.at(f":{minute:02d}").do(job, url=url, base_directory=base_directory)

    print(f"Scheduled job to download {url} at {minute} minutes past every hour.")
    print(f"Downloads will be saved to directory: {base_directory}")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
