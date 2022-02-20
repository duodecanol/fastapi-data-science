import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello_world():
    return {"hello": "world"}

if __name__ == '__main__':

    uvicorn.run("ch3_first_endpoint_01:app", host="0.0.0.0", port=7777, reload=True)
