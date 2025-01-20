import uvicorn
from fastapi import FastAPI

from com.study.basic.controller.BasicController import basic_app

app = FastAPI()
app.mount("/Study/basic",basic_app)

if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8085)