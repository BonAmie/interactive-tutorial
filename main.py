from Sql_connection import *

def GetAllOrdersByClientId(id):
    sql = Sql_connection()
    cnc = sql.Get_connection()
    q = f"exec GetAllOrdersByClientId {id}"
    r = sql.Get_from_db(cnc, q)
    for i in r:
        print(i.Name, i.Id)

GetAllOrdersByClientId(1)
