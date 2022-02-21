from fastapi import FastAPI, status
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    nb_views: int

class PublicPost(BaseModel):
    title: str

app = FastAPI()


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    return post


posts = {
    1: Post(title="Hello", nb_views=100),
}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    posts.pop(id, None)
    return None

@app.get("/posts/{id}")
async def get_post(id: int):
    return posts[id]

@app.get("/posts/public-posts/{id}", response_model=PublicPost)
async def get_public_post(id: int):
    return posts[id]


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("ch3_response_path_parameters:app", host="0.0.0.0", port=7777, reload=True, debug=True)
