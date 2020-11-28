import sys

import soundio

if __name__ == "__main__":
    
    wav_file_path = sys.argv[1] #Prog name at ind 0, first command at 1
    print("Trying to read file: " + wav_file_path + " as wav file")

    out = soundio.read_wav_file(wav_file_path)
    if out: #if it wasn't None:
        rate, data = out
        print("File was read. rate: " + str(rate))    
        print("file data: " + str(data))
    else:
        print("Failed opening file: " + str(wav_file_path))
