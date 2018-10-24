

def list_verification(my_list, id):
    try:
        return my_list[id - 1]
    except IndexError:
        return {"message": "Record with that ID missing"}
