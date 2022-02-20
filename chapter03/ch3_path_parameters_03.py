from enum import Enum
from fastapi import FastAPI

app = FastAPI()


class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"

@app.get("/users/{type}/{id}")
async def get_user(type: UserType, id: int):
    return {"type": type, "id": id}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("ch3_path_parameters_03:app", host="0.0.0.0", port=7777, reload=True)