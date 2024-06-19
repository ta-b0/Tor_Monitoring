import argparse
import schedule
import time
import os
import subprocess
from datetime import datetime
 
def download_site(url):
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    directory_name = current_time
 
    command = f'torsocks wget -rkp -l 1 {url} -P {directory_name}'
    try:
        subprocess.check_call(command, shell=True)
        print(f"Downloaded content from {url} and saved to {directory_name}")
    except subprocess.CalledProcessError:
        print(f"Failed to download content from {url}")
        if os.path.exists(directory_name):
            os.rmdir(directory_name)
 
def job(url):
    download_site(url)
 
def main():
    parser = argparse.ArgumentParser(description="Automatic downloader using torsocks and wget")
    parser.add_argument('-u', '--url', type=str, required=True, help='URL to download')
    parser.add_argument('-m', '--minute', type=int, required=True, help='Minute of the hour to run the download job')
 
    args = parser.parse_args()
 
    url = args.url
    minute = args.minute
 
    schedule.every().hour.at(f":{minute:02d}").do(job, url)
 
    print(f"Scheduled job to download {url} at {minute} minutes past every hour.")
 
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()
user@UbuntuTor
