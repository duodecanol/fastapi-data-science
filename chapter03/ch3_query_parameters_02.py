from enum import Enum
from fastapi import FastAPI, Path

class UserFormat(str, Enum):
    SHORT = "short"
    FULL = "full"

app = FastAPI()


@app.get("/users")
async def get_user(format: UserFormat):
    return {"format": format}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("ch3_query_parameters_02:app", host="0.0.0.0", port=7777, reload=True)
