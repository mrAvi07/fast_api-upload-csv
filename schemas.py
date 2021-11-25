from pydantic import BaseModel, Field


class StudentList(BaseModel):
    id         :   str 
    first_name :   str
    last_name  :   str
    mark       :   float


class StudentEntry(BaseModel):
    first_name  :   str     =   Field(..., example="lucifer")
    last_name   :   str     =   Field(..., example="Morning Star")
    mark        :   float     =   Field(..., example="76.89")


class StudentUpdate(BaseModel):
    id          :   str     =   Field(..., example="njakdjnasnd5a6d77ad")
    first_name  :   str     =   Field(..., example="lucifer")
    last_name   :   str     =   Field(..., example="Morning Star")
    mark        :   float     =   Field(..., example="76.89")



class StudentDelete(BaseModel):
    id  : str   =   Field(..., example="andkjaoijd12712hj1nkjnj")