from fastapi import FastAPI, HTTPException, Header
# Header buat informasi tambahan / information key
import pandas as pd

df = pd.read_csv('Financials.csv')
app = FastAPI()
API_KEY = "testingapi1234"

@app.get("/")
def home():
    return {"message": "This is my api. welcome"}

@app.get("/protected/{pos}")
def protected(pos:str,api_key:str=Header(None)):
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    else:
        return df[df['Country']==pos].to_dict(orient="records")