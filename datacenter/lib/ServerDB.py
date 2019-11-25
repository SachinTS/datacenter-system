# importing sqlite 3 for database operations
import sqlite3

# creating connection and cursor objects
con = sqlite3.connect('dataCenter.db')
c = con.cursor()


def fetchAllServer(self):
    try:
        c.execute("select * from servers")
    except Exception as e:
        print(str(e))


data = c.fetchall()
print(data)


def updateServerInfo(serverID, cpuCore, ram, increase):
    try:
        query = "update servers set RAM_Used = 'RAM_Used + increase' and CPU_Used = 'CPU_Used + " \
                "increase' where Status = '0' "
        c.execute(query)
        con.commit()

        query = "update servers set RAM_Used = 'RAM_Used - increase' and CPU_Used = 'CPU_Used - " \
                "increase' where Status = '1' "
        c.execute(query)
        con.commit()

    except Exception as e:
        print(str(e))

    c.execute("select * from servers")
    values = c.fetchall()
    print(values)


con.close()