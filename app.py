"""
#!/usr/bin/env python3.6
"""
import sys
import uvicorn

import logging

from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from logging.config import dictConfig
from log_config import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("airduka_lotto")

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

@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True, log_level="info")