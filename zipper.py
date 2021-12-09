import zlib
from os.path import exists
from os import remove


filename_in = "arima.pkl"
filename_out = "arima.compressed"
if exists(filename_out):
    remove(filename_out)
with open(filename_in, mode="rb") as fin, open(filename_out, mode="wb") as fout:
    data = fin.read()
    print("Compressing Pickle File for Version Control...")
    compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
    fout.write(compressed_data)