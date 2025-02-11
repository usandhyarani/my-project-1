import pickle
from fastapi import FastAPI
from pydantic import BaseModel
with open('iris_model.pkl','rb') as f:
  model = pickle.load(f)
app = FastAPi()
classIrisInput(Basemodel):
sl:float
sw:float
pl:float
pw:float
@app.get("/")
def read_root():
  return{'message':'welcome to fastapi'}

@app.post("/predict/")
def predict(data:IrisInput):
  Input_data = [[data.sl,data.sw,data.pl,data.pw]]
  prediction = model.predict(inputdata)[0]
  return {prediction is ':int(prdiction)}
