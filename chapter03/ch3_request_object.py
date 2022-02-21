from fastapi import FastAPI, Request

app = FastAPI()

# Sometimes, you might find that you need to access a raw request object with all of the data
# associated with it. That's possible. Simply declare an argument on your path operation
# function type hinted with the Request class:
@app.get("/")
async def get_request_object(request: Request):
    return {
        "path": request.url.path,
        "base_url": request.base_url.path,
        "client_port": request.client.port,
        "method": request.method,
        "host": request.client.host,
    }

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("ch3_request_object:app", host="0.0.0.0", port=7777, reload=True, debug=True)
