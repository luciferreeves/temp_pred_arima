import sys
import requests
import subprocess
from os.path import exists

subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def download(url, filename):
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50*downloaded/total)
                sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50-done)))
                sys.stdout.flush()
    sys.stdout.write('\n')

if not exists('database.db'):
    print('[*] Downloading database.db')
    download("https://github.com/luciferreeves/temp_pred_arima/releases/download/large_files/database.db", 'database.db')

if not exists('GlobalLandTemperaturesByCity.csv'):
    print('[*] Downloading GlobalLandTemperaturesByCity.csv')
    download("https://github.com/luciferreeves/temp_pred_arima/releases/download/large_files/GlobalLandTemperaturesByCity.csv", 'GlobalLandTemperaturesByCity.csv')

print('[*] Done! Please run `python3 app.py` to start the application.')
