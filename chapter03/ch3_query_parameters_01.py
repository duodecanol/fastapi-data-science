from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/users/")
async def get_user(page: int = 1, size: int = 10):
    return {"page": page, "size": size}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("ch3_query_parameters_01:app", host="0.0.0.0", port=7777, reload=True)
