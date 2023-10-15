# main.py
import uvicorn
from fastapi import FastAPI, File, UploadFile, Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from core.voice_process import save_file, evaluate  # 作成した関数をインポート


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

def get_current_user(token: str = Security(oauth2_scheme)):
    if token != "my_secret_token":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"username": "john"}

@app.get("/users/me", response_model=dict)
def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user

@app.post("/token")
def get_token(username: str, password: str):
    if username == "john" and password == "password":
        return {"access_token": "my_secret_token", "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Unauthorized")



@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.post("/upload")
async def upload_files(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    path1 = save_file(file1)
    path2 = save_file(file2)
    score = evaluate(path1,path2)
    print(score)
    return {"filename1": file1.filename, "filename2": file2.filename}

if __name__ == "__main__":
    uvicorn.run(app = "main:app", host="0.0.0.0", reload=True, port = 8000, log_level = "debug")
