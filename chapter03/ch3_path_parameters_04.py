from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/users/{id}")
async def get_user(id: int = Path(..., ge=1)):
    return {"id": id}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("ch3_path_parameters_04:app", host="0.0.0.0", port=7777, reload=True)
