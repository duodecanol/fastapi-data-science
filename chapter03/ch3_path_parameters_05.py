from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/license-plate/{license}")
async def get_license_plate(license: str = Path(..., min_length=9, max_length=9)):
    return {"license": license}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("ch3_path_parameters_05:app", host="0.0.0.0", port=7777, reload=True)
