# For request object with all of the data associated with it

from fastapi import FastAPI,Request


app = FastAPI()

@app.get('/')
async def get_request_object(request:Request):
    # this method return the path of request
    return {'path':request.url.path}