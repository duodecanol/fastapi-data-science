from fastapi import FastAPI, Body
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
class Company(BaseModel):
    name: str

app = FastAPI()


@app.post("/users")
async def create_user(user: User, company: Company):
    return {"user": user, "company": company}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("ch3_request_body_03:app", host="0.0.0.0", port=7777, reload=True)
