from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/license-plate/{license}")
async def get_license_plate(license: str = Path(..., regex=r"^\w{2}-\d{3}-\w{2}$")):
    return {"license": license}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("ch3_path_parameters_06:app", host="0.0.0.0", port=7777, reload=True)
