from fastapi import FastAPI
from pydantic import BaseModel
# import mysql.connector
import pymysql

app = FastAPI()




class Msg(BaseModel):
    msg: str


@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to  FastAPI!"}


@app.get("/data")
async def get_marked_systems():
    
    connection = pymysql.connect( host='containers-us-west-32.railway.app', user='root', passwd='Jyfcd452Xe3tmMsFLYDY', port=5522, db='railway' )
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `name` FROM `marked_systems` WHERE `id`=%s"
        cursor.execute(sql, ('1',))
        result = cursor.fetchone()
        print(result)
    # doQuery( myConnection )
    # myConnection.close()
    # cnx = mysql.connector.connect(user='root', password='Jyfcd452Xe3tmMsFLYDY', host='containers-us-west-32.railway.app:5522', database='railway')
    # cursor = cnx.cursor()

    # query = 'SELECT * FROM marked_systems'
    # cursor.execute(query)

    # rows = []
    # for row in cursor:
    #     print(row)
    #     rows.append(row)

    return {"data": result}
    cursor.close()
    cnx.close()

@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}