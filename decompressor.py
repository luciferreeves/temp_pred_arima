from os.path import exists
import zlib

def decompress_arima():
    if not exists('arima.pkl'):
        if not exists('arima.compressed'):
            raise FileNotFoundError('arima.compressed not found')
        else:
            print('Decompressing arima.compressed')
            with open('arima.compressed', 'rb') as f:
                data = zlib.decompress(f.read())
            with open('arima.pkl', 'wb') as f:
                f.write(data)

decompress_arima()