from typing import Optional
from fastapi import Cookie, FastAPI, Header


app = FastAPI()

# @app.get('/')
# async def get_header(hello:str=Header(...)):
#     return {'hello':hello}


@app.get('/')
async def get_header(user_agent:str = Header(...)):
    return {'user_agent':user_agent}


@app.get('/cookie')
async def get_cookie(hello:Optional[str]=Cookie(None)):
    return {'hello':hello}