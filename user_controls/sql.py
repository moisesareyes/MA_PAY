def conector():
    import mysql.connector 
    mydb=mysql.connector.connect(host="192.168.0.100",user="root",password="",database="test",autocommit=True)
    off=mydb.cursor()
    off.execute("SET SESSION query_cache_type = OFF")
    return mydb
