from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/users")
async def create_user(name: str = Form(...), age: int = Form(...)):
    return {"name": name, "age": age}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("ch3_form_data_01:app", host="0.0.0.0", port=8888, reload=True)


# Pay attention to how the Content-Type header and the body data representation have
# changed in the request. You can also see that the response is still provided in JSON. Unless
# specified otherwise, FastAPI will always output a JSON response by default, no matter the
# form of the input data.

# Content-Type: application/json
#         =>
# Content-Type: application/x-www-form-urlencoded; charset=utf-8
