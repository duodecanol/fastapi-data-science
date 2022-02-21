from fastapi import FastAPI, File, UploadFile
from typing import List

app = FastAPI()


@app.post("/files")
async def upload_file(files: List[UploadFile] = File(...)):
    return [
        {"file_name": file.filename, "content_type": file.content_type}
        for file in files
    ]

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("ch3_file_uploads_03:app", host="0.0.0.0", port=8888, reload=True)
