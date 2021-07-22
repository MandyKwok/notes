# reference: https://towardsdatascience.com/a-layman-guide-for-data-scientists-to-create-apis-in-minutes-31e6f451cd2f

# ----------------------------------------
# GET
# ----------------------------------------

# from fastapi import FastAPI

# app = FastAPI()
# @app.get("/predict")

# def predict_complex_model(age: int, sex: str):

#     # Assume a big and complex model here. For this test I am using a simple rule based model
    
#     if age < 10 or sex == 'F':
#         return {'survived': 1}
#     else:
#         return {'survived': 0}

# ----------------------------------------
# PUT
# ----------------------------------------
from fastapi import FastAPI
from pydantic import BaseModel

class Input(BaseModel):
    age : int
    sex : str
        
app = FastAPI()
@app.put("/predict")

def predict_complex_model(d: Input):
    if d.age < 10 or d.sex == 'F':
        return {'survived' : 1}
    else:
        return {'survived' : 0}