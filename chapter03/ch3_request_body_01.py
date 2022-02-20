from fastapi import FastAPI, Body

app = FastAPI()


@app.post("/users")
async def create_user(name: str = Body(...), age: int = Body(...)):
    return {"name": name, "age": age}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("ch3_request_body_01:app", host="0.0.0.0", port=7777, reload=True)
