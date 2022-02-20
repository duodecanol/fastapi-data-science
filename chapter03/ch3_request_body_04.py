from fastapi import FastAPI, Body
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

app = FastAPI()


@app.post("/users")
async def create_user(user: User, priority: int = Body(..., ge=1, le=3)):
    return {"user": user, "priority": priority}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("ch3_request_body_04:app", host="0.0.0.0", port=7777, reload=True)
