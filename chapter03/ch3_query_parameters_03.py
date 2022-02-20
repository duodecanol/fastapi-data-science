from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/users")
async def get_user(page: int = Query(1, gt=0), size: int = Query(10, le=100)):
    return {"page": page, "size": size}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("ch3_query_parameters_03:app", host="0.0.0.0", port=7777, reload=True)
