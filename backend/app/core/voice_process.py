# core/voice_process.py
import numpy as np
import shutil
from tempfile import NamedTemporaryFile
from fastapi import UploadFile
import librosa
import matplotlib.pyplot as plt
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

def save_file(file: UploadFile):
    with NamedTemporaryFile(delete=False) as buffer:
        shutil.copyfileobj(file.file, buffer)
    tmp_file_name = buffer.name
    return tmp_file_name

def apply_average_filter(y, filter_size=5):
    # 平均化フィルタのカーネルを作成
    kernel = np.ones(filter_size) / filter_size
    
    # 畳み込みを適用
    y_filtered = np.convolve(y, kernel, 'same')
    
    return y_filtered
def compare(y1,y2,sr):
    y1 = apply_average_filter(y1)
    y2 = apply_average_filter(y2)
    mfcc1 = librosa.feature.mfcc(y=y1, sr=sr, n_mfcc=13)
    mfcc2 = librosa.feature.mfcc(y=y2, sr=sr, n_mfcc=13)
    distance, _ = fastdtw(mfcc1.T, mfcc2.T, dist=euclidean)
    """
    pitch1, mag1 = librosa.piptrack(y=y1, sr=sr)
    pitch2, mag2 = librosa.piptrack(y=y2, sr=sr)
    distance, _ = fastdtw(mag1.T, mag2.T, dist=euclidean)
    """
    return distance



def plot_audio(y, path):
    plt.figure(figsize=(10, 4))
    plt.plot(y)
    plt.title('Waveform')
    plt.xlabel('Time [samples]')
    plt.ylabel('Amplitude')

    # 保存先のパスが拡張子を含まない場合は、PNGとして保存する。
    if not path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        path += '.png'

    plt.savefig(path)


def evaluate(path1, path2):
    y1, sr1 = librosa.load(path1, sr=None)
    y2, sr2 = librosa.load(path2, sr=None)
    plot_audio(y1, path="data/tmp1.png")
    plot_audio(y2, path="data/tmp2.png")
    score = compare(y1,y2,sr1)
    
    return score