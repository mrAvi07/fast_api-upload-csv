from fastapi import FastAPI, File, UploadFile
from typing import List
import uuid
import py_functions
import pandas as pd
from db import database, students
import schemas



app = FastAPI()


# connect to database
@app.on_event("startup")
async def startup():
    await database.connect()


# disconnect with database
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# get all students details
@app.get('/students', response_model=List[schemas.StudentList], tags=["Student"])
async def get_students():
    query = students.select()
    return await database.fetch_all(query)


# get student details using student id
@app.get('/student/{student_id}', response_model=schemas.StudentList, tags=["Student"])
async def get_student_by_id(student_id: str):
    query = students.select().where(students.c.id == student_id)
    return await database.fetch_one(query)



# Upload new student details
@app.post('/student', response_model=schemas.StudentList, tags=["Student"])
async def student_post(student: schemas.StudentEntry):
    gID = str(uuid.uuid1())
    query = students.insert().values(
        id          =   gID                ,
        first_name  =   student.first_name ,
        last_name   =   student.last_name  ,
        mark        =   student.mark       ,
    )

    await database.execute(query)

    return {
        "id" : gID,
        **student.dict(),
    }


# update student details
@app.put('/student', response_model=schemas.StudentList, tags=["Student"])
async def student_update(student: schemas.StudentUpdate):
    gID = student.id
    query = students.update().\
        where(students.c.id == gID).\
        values(
            first_name = student.first_name,
            last_name  = student.last_name ,
            mark       = student.mark      ,
        )

    await database.execute(query)

    return {
        "id" : gID,
        **student.dict(),
    }


# delete student details
@app.delete('/student', tags=["Student"])
async def student_delete(student: schemas.StudentDelete):
    gID = student.id
    query = students.delete().where(students.c.id == gID) 
    await database.execute(query)
    
    return {
        "message" : "Student details has been deleted" 
    }

            

# csv file upload
@app.post('/files', tags=["Files"])
async def student_data(file_data: UploadFile = File(...)):
    try:
        df = pd.read_csv(file_data.file)
        df['year'] = 2020
        for index, row in df.iterrows():
            gID = str(uuid.uuid4())
            query = students.insert().values(
                id         = gID,
                first_name = row.first_name,
                last_name  = row.last_name,
                mark       = row.marks,
            )
        
            await database.execute(query)

        return {'status' : 'succes'}
    
    except:
        return {'status' : 'error'}
