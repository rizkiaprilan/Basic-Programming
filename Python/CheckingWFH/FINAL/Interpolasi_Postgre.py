import psycopg2
from pprint import pprint 
import os

# connect to database
con = psycopg2.connect(
    dbname='gis',
    user='sde',
    host='gis105-db.udata.id',
    password='47HAz123',
    port='5432'
)

def get_data():         #get all data
    data = []
    cur = con.cursor()

    query = "select * from dx_telkom_wfh_stg1 where wfh_date != 100 order by wfh_date, reg, jam"
    cur.execute(query)

    rows = cur.fetchall()
    
    for r in rows:
        line= []
        for i in range(0,6):
            line.append(int(r[i]))  #masukkan datanya ke variabel data
            if i==5:
                line.append(str(r[6]))
        data.append(line)

    cur.close()
    # close connection
    
    return data

def insert_data(reg,jam,device,wfh_date,activity,usage,status):         #insert data
    cur = con.cursor()

    cur.execute("""INSERT INTO dx_telkom_wfh_stg1 (reg,jam,sum_countd_device,wfh_date,sum_act_sec,sum_usage,status) VALUES (%s, %s, %s, %s, %s, %s, %s);""",(reg, jam, device,wfh_date,activity,usage,status))
    
    con.commit()
    cur.close()

def convertToInteger(stmt):             #convert ke integer

    if isinstance(stmt,str):                    
        statementNew = stmt.replace(",","")
        result = int(statementNew) 
    else:
        result = int(stmt)
    return  result

def calculate_Count_Update(data,index):
    update = 0
    for a in range(1,len(data)):
        if data[index - a][6] == "UPDATED":
            update = update - 1
        else:
            break
    return update

class Interpolasi:  #parent

    def __init__(self,data,index,jam):
        self.data = data
        self.index = index
        self.jam = jam

    def makeREG(self):
        if(self.jam==0):
            statement = self.data[self.index+1][0]
        else:
            statement = self.data[self.index-1][0]
        return statement

    def makeWFH(self):
        if(self.jam==0):
            statement = self.data[self.index+1][3]
        else:
            statement = self.data[self.index-1][3]
        return statement

class Device(Interpolasi):

    def __init__(self,data,index,jam):   #constractor
        super().__init__(data,index,jam) #property parent

    def rumus_kosong(self):

        status = 0
        jmlD = []
        if self.data[self.index-1][6] == "UPDATED":
            status = calculate_Count_Update(self.data,self.index) + 3
        else:
            status = 3
        for i in range(0,len(self.data)):
            if self.data[i][0] == self.data[self.index][0] and self.data[i][1] == self.data[self.index][1] and self.data[i][3] == self.data[self.index][3]:
                break
            elif self.data[i][0] == self.data[self.index][0] and self.data[i][1] == self.data[self.index][1]:
                jmlD.append(convertToInteger(self.data[i-status][2]))
        return round(sum(jmlD)/len(jmlD))

class Activity(Interpolasi):
    
    def __init__(self,data,index,jam):
        super().__init__(data,index,jam)

    def rumus_kosong(self):
        status = 0
        jmlA = []
        if self.data[self.index-1][6] == "UPDATED":
            status = calculate_Count_Update(self.data,self.index) + 3
        else:
            status = 3

        for i in range(0,len(self.data)):
            if self.data[i][0] == self.data[self.index][0] and self.data[i][1] == self.data[self.index][1] and self.data[i][3] == self.data[self.index][3]:
                break
            elif self.data[i][0] == self.data[self.index][0] and self.data[i][1] == self.data[self.index][1]:
                jmlA.append(convertToInteger(self.data[i-status][4]))
        return round(sum(jmlA)/len(jmlA))

class Usage(Interpolasi):
    
    def __init__(self,data,index,jam):
        super().__init__(data,index,jam)
        
    def rumus_kosong(self):
        status = 0
        jmlU = []
        if self.data[self.index-1][6] == "UPDATED":
            status = calculate_Count_Update(self.data,self.index) +3
        else:
            status = 3
        for i in range(0,len(self.data)):
            if self.data[i][0] == self.data[self.index][0] and self.data[i][1] == self.data[self.index][1] and self.data[i][3] == self.data[self.index][3]:
                break
            elif self.data[i][0] == self.data[self.index][0] and self.data[i][1] == self.data[self.index][1]:
                jmlU.append(convertToInteger(self.data[i-status][5]))
        return round(sum(jmlU)/len(jmlU))

updated = "UPDATED"
def check(start):
    
    data = get_data()
    jam = data[start][1]
    
    for index in range(start,len(data)):
        device = Device(data,index,jam)
        activity = Activity(data,index,jam)
        usage = Usage(data,index,jam)
        interpolasi = Interpolasi(data,index,jam)
        if data[index][1] != jam:
            if data[index-1][6] == "UPDATED":
               
                insert_data(interpolasi.makeREG(),jam,device.rumus_kosong(),interpolasi.makeWFH(),activity.rumus_kosong(),usage.rumus_kosong(),updated)
            else:
              
                insert_data(interpolasi.makeREG(),jam,device.rumus_kosong(),interpolasi.makeWFH(),activity.rumus_kosong(),usage.rumus_kosong(),updated)
            print("row: " + str(index+1) + " UPDATED")
            return 1
        
        if jam != 23:
            jam=jam+1
        else:
            jam = 0

start = 0                   #start PENTING!!

while check(start) == 1:
    check(start)

data = get_data()   
x = len(data)-1
interpolasi2 = Interpolasi(data,x,23)
device2 = Device(data,x,23)
activity2 = Activity(data,x,23)
usage2 = Usage(data,x,23)

if data[x][1] != 23:                                                                                        #kalo data terakhir tidak di jam 23
    insert_data(interpolasi2.makeREG(),23,device2.rumus_kosong(),interpolasi2.makeWFH(),activity2.rumus_kosong(),usage2.rumus_kosong(),updated)

print("The Data has been UPDATED\n\n")
os.system('pause')      #hold terminal
data = get_data()
con.close()