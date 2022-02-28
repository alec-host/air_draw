"""
#!/usr/bin/env python3.6
"""

import sys
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import conn.config

sys.path.insert(0,conn.config.REGISTER_DIR)
import register_api
sys.path.insert(0,conn.config.DRAW_DIR)
import draw_api

app = FastAPI(openapi_url="/api/v1/openapi.json")

origins = [
	"http://localhost",
	"http://localhost:8000",
    "https://c914-41-139-151-158.ngrok.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(register_api.register_router)
app.include_router(draw_api.draw_router)

@app.get('/')
def root_api():
        return {"message":"airduka.com"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=False, log_level="info")