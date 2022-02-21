from fastapi import FastAPI, File

app = FastAPI()


@app.post("/files")
async def upload_file(file: bytes = File(...)):
    return {"file_size": len(file)}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("ch3_file_uploads_01:app", host="0.0.0.0", port=8888, reload=True)
