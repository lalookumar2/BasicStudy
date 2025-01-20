from fastapi import FastAPI
from starlette.requests import Request

from com.study.basic.service.BasicService import getStudentDetailsService

basic_app = FastAPI()


@basic_app.get("/test")
async def test():
    return {"status":"sucess"}

@basic_app.post("/getStudentDetails")
async def getStudentDetails(input:Request):
    data=await input.json()
    result=getStudentDetailsService(data)
    return result
