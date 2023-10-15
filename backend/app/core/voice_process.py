import shutil
from tempfile import NamedTemporaryFile
from fastapi import UploadFile
import librosa

def save_file(file: UploadFile):
    with NamedTemporaryFile(delete=False) as buffer:
        shutil.copyfileobj(file.file, buffer)
    tmp_file_name = buffer.name
    return tmp_file_name

def evaluate(path1, path2):
    y1, sr1 = librosa.load(path1, sr=None)
    return 3