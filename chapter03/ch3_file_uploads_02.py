from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files")
async def upload_file(file: UploadFile = File(...)):
    return {"file_name": file.filename, "content_type": file.content_type}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("ch3_file_uploads_02:app", host="0.0.0.0", port=8888, reload=True)
