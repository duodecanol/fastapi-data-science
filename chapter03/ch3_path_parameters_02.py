from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{type}/{id}")
async def get_user(type: str, id: int):
    return {"type": type, "id": id}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("ch3_path_parameters_02:app", host="0.0.0.0", port=7777, reload=True)