from fastapi import FastAPI
from pydantic import BaseModel
from database_connection_handler import DbConnectionHandler
import datetime

app = FastAPI()
db = DbConnectionHandler()
cursor, db_connection = db.connect_to_db()


class UserParameters(BaseModel):
    user_name: str
    user_phone_number: int
    user_email: str


@app.get('/')
async def default():
    return {"status": "UP", "datetime": datetime.datetime.now()}


@app.get("/notes")
async def notes():
    cursor.execute("SELECT * FROM notes")
    response = cursor.fetchall()
    return response


@app.post("/notes/{user_id}")
async def add_note(user_id: int, title: str, data: str):
    response = {"success": True}
    cursor.execute("INSERT INTO notes (user_id, title, data) VALUES(%s, %s, %s)", (user_id, title, data))
    db_connection.commit()
    # records = cursor.fetchall()
    # response.update({'records': records})
    return response


@app.patch("/update_notes/{note_id}")
async def update_notes(note_id: int, data: dict):
    response = {"success": True}
    keys = ()
    for key, value in data.items():
    cursor.execute("UPDATE notes SET ")


@app.delete("/delete_note/{user_id}")
async def delete_note(user_id: int, title: str):
    response = {"success": True}
    cursor.execute("DELETE FROM notes WHERE title = %s AND user_id = %s", (title, user_id))
    deleted = cursor.rowcount
    response.update({'count': deleted})
    db_connection.commit()
    return response



# @app.patch("/notes/update/{user_id}")
# async def patch_notes_data(user_id, record_dict: dict):
#     cursor.execute("UPDATE TABLE notes SET ")

def unpack_json(response):
    if 'records' not in response:
        return response

    new_records = []
    for record in response['records']:
        if 'details' not in record:
            new_records.append(record)
        else:
            # if 'details' field is present in record
            new_record = {}
            if record.get('details') is not None:
                for key, val in record['details'].items():
                    new_record.update({key: val})
            del record['details']
            new_record.update(record)
            new_records.append(new_record)
    response['records'] = new_records
    return response


@app.get("/notes/{note_id}")
async def notes_by_id(note_id: int):
    response = {"success": True}
    cursor.execute(f"SELECT * FROM notes WHERE id={note_id};")
    # print(response)
    records = cursor.fetchall()
    # response.update({'total_count': cursor.rowcount})
    response.update({'records': records})
    # response = unpack_json(response)
    return response


# @app.get("/dev/{user_id}")
@app.put("/dev/{user_id}")
async def dev(user_id: int, user_data: UserParameters):
    return {"comment": "You Have Entered Dev Environment", "user_id": user_id, "email": user_data.user_email, "phone_number": user_data.user_phone_number}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]
