from fastapi import FastAPI

from pydantic import BaseModel

class Post(BaseModel):
    title : str
    nb_views: int

app = FastAPI()

# Dummy Database

posts={
    1: Post(title="Hello",nb_views=100),
}

@app.get('/posts/{id}')
async def get_post(id:int):
    return posts[id]


class PublicPost(BaseModel):
    title : str


@app.get('/post/{id}',response_model=PublicPost)
async def get_post(id:int):
    '''
    here response_model in FastAPI automatically converted our Post instance into a PublicPost instance before
    serializing it. Now our private data is safe
    '''
    return posts[id]
