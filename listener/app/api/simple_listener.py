from fastapi import FastAPI, status
from starlette.responses import Response
from db_utils import *
from models import *

app = FastAPI(title="Listener", version="1.0.0")

@app.get("/")
async def root() -> dict:
    return({"message": "I am ROOT..."})

@app.post("/post_data_to_db", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def post_data_to_db(data: InputData) -> Response:

    connection = db_connect()

    table_name = 'kewt_data'
    columns = list(data.body.keys())
    check_table(connection, table_name, columns)
    insert_data(connection, table_name, data.body)

    db_disconnect(connection)

    return(Response(status_code=status.HTTP_204_NO_CONTENT))
