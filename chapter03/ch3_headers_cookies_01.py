from typing import Optional

from fastapi import FastAPI, Header, Cookie

app = FastAPI()

@app.get("/hello")
async def get_header(hello: str = Header(...)):
    return {"hello": hello}

@app.get("/header")
async def get_header2(user_agent: str = Header(...)):
    return {"user_agent": user_agent}

@app.get("/cookies")
async def get_cookie(hello: Optional[str] = Cookie(None)):
    return {"hello": hello}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("ch3_headers_cookies_01:app", host="0.0.0.0", port=7777, reload=True)
