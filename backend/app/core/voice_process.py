import shutil
from tempfile import NamedTemporaryFile
from fastapi import UploadFile

def save_file(file: UploadFile):
    with NamedTemporaryFile(delete=False) as buffer:
        shutil.copyfileobj(file.file, buffer)
    tmp_file_name = buffer.name
    return tmp_file_name
