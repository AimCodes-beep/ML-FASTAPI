from fastapi import FastAPI,Form,File,Path,Query,Response,BackgroundTasks
from pydantic import BaseModel,EmailStr,Field
from fastapi.responses import HTMLResponse
from typing import Annotated,List
import joblib
import pandas as pd
#LOADING THE MODEL
model=joblib.load('k_means_wholesale_model.pkl')
print(model) 

#CREATING FASTAPI INSTANCE
app=FastAPI()
#BACKGROUND TASK 1
def save_details(Channel:int,Region:int,Fresh:int,Milk:int,Grocery:int):
    message=f"SAVE DETAILS {Channel} :{Region} FRESH QUALITY:{Fresh},MILK QUALITY:{Milk},Grocery:{Grocery} \n"
    with open('New_Cs_data.txt','a') as f:
        f.write(message)
#WELCOME API
@app.get('/home')
async def welcome_home():
    return {"Messsage":"WELCOME TO WHOLESALE CUSTOMER SEGEMENTATION PROJECT"}
#FORM API
#@app.get('/',response_class=HTMLResponse
@app.get('/',response_class=HTMLResponse)
async def get_form():
    return """
    <html>
    <head>
    <title>WHOLESALE CUSTOMER SEGEMENTATION PROJECT</title>
    </head>
    <body>
    <h1>WHOLESALE CUSTOMER SEGEMENTATION PREDICTION FORM </h1>
    <form action='/submit' method="post">
    <label for="Channel">Channel</label><br>
    <input type="text" name="Channel" id="Channel"><br><br>
    <label for="Region">Region</label><br>
    <input type="text" name="Region" id="Region"><br><br>
    <label for="Fresh">Fresh</label><br>
    <input type="text" name="Fresh" id="Fresh"><br><br>
    <label for="Milk">Milk</label><br>
    <input type="text" name="Milk" id="Milk"><br><br>
    <label for="Grocery">Grocery</label><br>
    <input type="text" name="Grocery" id="Grocery"><br><br>
    <label for="Frozen">Frozen</label><br>
    <input type="text" name="Frozen" id="Frozen"><br><br>
    <label for="Detergents_Paper">Detergent><br>
    <input type="text" name="Detergents_Paper" id="Detergents_Paper"><br><br>
    <label for="Delicassen">Delicassen</label><br>
    <input type="text" name="Delicassen" id="Delicassen"><br><br>
    <input type="submit" value='Submit'>
    </form>
    <div>
    <p>CREATED BY DS AIMAN</p>
    </body>
    </html>
"""
@app.post("/submit")
async def submit_data(Channel: Annotated[int, Form()],Region: Annotated[int, Form()], Fresh: Annotated[float, Form()], Milk: Annotated[float, Form()],Grocery: Annotated[float, Form()],Frozen: Annotated[float, Form()],Detergents_Paper: Annotated[float, Form()],Delicassen: Annotated[float, Form()],b1:BackgroundTasks):
    
    input_df = pd.DataFrame([{
        "Channel": Channel,
        "Region": Region,
        "Fresh": Fresh,
        "Milk": Milk,
        "Grocery": Grocery,
        "Frozen": Frozen,
        "Detergents_Paper": Detergents_Paper,
        "Delicassen": Delicassen
    }])

    b1.add_task(save_details,Channel,Region,Fresh,Milk,Grocery)
    prediction = model.predict(input_df)

    return {"cluster": f"This customer belong to Cluster {int(prediction[0])}"}
