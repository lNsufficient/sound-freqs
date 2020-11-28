from scipy.io import wavfile

def read_wav_file(wav_file_path):
    """Assume file is wav and read using scipy

    Parameters
    ----------
    wav_file_path : str, absolute path to wav file
    
    Returns
    -------
    rate : int, sample rate
    data : numpy array, sound recording data
    """
    rate, data = wavfile.read(wav_file_path)
    return rate, data
