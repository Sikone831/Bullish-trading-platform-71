from fastapi import FastAPI
from typing import List
import os

app = FastAPI()

@app.get("/screener/bullish")
async def bullish_screener(tickers: str):
    return {"tickers_received": tickers.split(",")}
