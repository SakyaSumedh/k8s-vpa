import os

from fastapi import FastAPI
import psutil
from pydantic import BaseModel
import uvicorn

LARGE_LIST: list[int] | None = None


def memory_usage() -> float:
    process = psutil.Process(os.getpid())
    memory = process.memory_info().rss / 1024 / 1024  # Convert bytes to MB
    return memory


class Consumer(BaseModel):
    size: int = 0


app = FastAPI()


@app.get("/")
async def memory_usage_metrics():
    memory_utilization = memory_usage()
    return {
        "memory_utilization": f"{memory_utilization} MB"
    }


@app.get("/health")
async def health_check():
    return {"message": "Hello World"}



@app.post("/memory-consume")
async def memory_consumer(data: Consumer):
    global LARGE_LIST
    size_in_mb = data.size
    elements_count = size_in_mb * (1024 * 1024 // 4)  # 1 int = 4 bytes
    LARGE_LIST = [0] * elements_count
    return {"message": "Success"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)