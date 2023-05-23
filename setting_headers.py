from fastapi import FastAPI,Response

app = FastAPI()

@app.get('/')
async def custom_header(response:Response):
    response.headers['Custom_Header']="Custom-Header-Value"
    return {'hello':'world'}