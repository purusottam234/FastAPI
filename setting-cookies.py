'''
Cookies can be particularly useful when you want to maintain the user's state within
the browser between each of their visits

To prompt the browser to save some cookies in our response, we could, of course
build our own Set-Cookie header and set it in the headers dictonary
'''

from fastapi import FastAPI,Response

app = FastAPI()


@app.get('/')
async def custom_cookie(response:Response):
    response.set_cookie('cookie-name','cookie-value',max_age=86400)
    return {'hello':'world'}
