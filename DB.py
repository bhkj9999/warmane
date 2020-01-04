import sqlite3 as sDB

def TODO():
    first = 'dateType, auto_increcement'
    Second = 'UPDATE WHERE ID to update data'
    return first, Second

def createDataBase():
    # create connection
    conn = sDB.connect('sqlite3.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE successinfo(id, date, request_status_code, md5, latest_event)''')
    conn.commit()

    conn.close()

    return

def dataBaseRead():
    conn = sDB.connect('sqlite3.db')
    c = conn.cursor()

    data = c.execute("SELECT * FROM successinfo")
    savedData = data.fetchone()
    date = savedData[0]
    request_status_code = savedData[1]
    md5 = savedData[2]
    nEvent = savedData[3]

    return date, request_status_code, md5, nEvent

def dataBaseWrite(date, res_code, md5, nEvent):
    conn = sDB.connect('sqlite3.db')
    c = conn.cursor()

    # c.execute("INSERT INTO successinfo VALUES ('2020-01-05',200,'RHAT')")
    c.execute("INSERT INTO successinfo VALUES ({date},{res_code},{md5},{nEvent})")

    conn.commit()
    conn.close()

    return 