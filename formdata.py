# Form data :
'''
This method to retrieve form data fields to retrieve singular JSON properties

'''

from fastapi import FastAPI,Form,File,UploadFile


app = FastAPI()

@app.post('/users')
async def create_user(name:str=Form(...),age:int=Form(...)):
    return {'name':name,'age':age}


# FIle Upload

# @app.post('/files')
# async def upload_file(file:bytes = File(...)):
#     return {'file_sizes':len(file)}

@app.post('/files')
async def upload_file(file:UploadFile=File(...)):
    return {'file_name':file.filename,'content_type':file.content_type}

from typing import List

@app.post('/multiple_files')
async def upload_multiple_files(files:List[UploadFile]=File(...)):
    return [{'file_name':file.filename,'content_type':file.content_type} for file in files]

 