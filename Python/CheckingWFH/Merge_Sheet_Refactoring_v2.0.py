import gspread 
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import os

print("\n[Welcome to Automate Interpolasi App]\n")
start = int(input("Starting from what row? ")) - 2   #PENTING!!!
print('\n')

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(".\\FIXED\\creds.json",scope)
client = gspread.authorize(creds)
sheet = client.open("DX_V_TELKOM_WFH Interpolasi2").get_worksheet(0) #mulai dari index 0
#=======================================================================================================
# sheet.update_cell(1,8,"STATUS")

def convertToInteger(stmt):

    if isinstance(stmt,str):                    #kalo dia string
        statementNew = stmt.replace(",","")
        result = int(statementNew) 
    else:
        result = int(stmt)
    return  result

def calculate_Count_Update(data,index):
    update = 0
    for a in range(1,len(data)):
        if data[index - a]["STATUS"] == "UPDATED":
            update = update - 1
        else:
            break
    return update

class Interpolasi:  #parent

    def __init__(self,data,index,jam):
        self.data = data
        self.index = index
        self.jam = jam

    def makeKey(self):
        if(self.jam==0):
            statement = str(self.data[self.index+1]["REG"]) + "-" + str(self.jam) + "-" + str(self.data[self.index+1]["WFH_DATE"])
        else:
            statement = str(self.data[self.index-1]["REG"]) + "-" + str(self.jam) + "-" + str(self.data[self.index-1]["WFH_DATE"])
        return statement

    def makeREG(self):
        if(self.jam==0):
            statement = self.data[self.index+1]["REG"]
        else:
            statement = self.data[self.index-1]["REG"]
        return statement

    def makeWFH(self):
        if(self.jam==0):
            statement = self.data[self.index+1]["WFH_DATE"]
        else:
            statement = self.data[self.index-1]["WFH_DATE"]
        return statement

class Device(Interpolasi):

    def __init__(self,data,index,jam):   #constractor
        super().__init__(data,index,jam) #property parent
       

    def rumus_kosong(self):

        status = 0
        jmlD = []
        if self.data[self.index-1]["STATUS"] == "UPDATED":
            status = calculate_Count_Update(self.data,self.index) + 3
        else:
            status = 3
        for i in range(0,len(self.data)):
            if self.data[i]["REG"] == self.data[self.index]["REG"] and self.data[i]["JAM"] == self.data[self.index]["JAM"] and self.data[i]["WFH_DATE"] == self.data[self.index]["WFH_DATE"]:
                break
            elif self.data[i]["REG"] == self.data[self.index]["REG"] and self.data[i]["JAM"] == self.data[self.index]["JAM"]:
                jmlD.append(convertToInteger(self.data[i-status]["SUM_COUNTD_DEVICE"]))
        return round(sum(jmlD)/len(jmlD))

class Activity(Interpolasi):
    
    def __init__(self,data,index,jam,totalActivity=None,calculateA=None):
        super().__init__(data,index,jam)
        self.totalActivity = totalActivity
        self.calculateA = calculateA

    def rumus_kosong(self):
        status = 0
        jmlA = []
        if self.data[self.index-1]["STATUS"] == "UPDATED":
            status = calculate_Count_Update(self.data,self.index) + 3
        else:
            status = 3

        for i in range(0,len(self.data)):
            if self.data[i]["REG"] == self.data[self.index]["REG"] and self.data[i]["JAM"] == self.data[self.index]["JAM"] and self.data[i]["WFH_DATE"] == self.data[self.index]["WFH_DATE"]:
                break
            elif self.data[i]["REG"] == self.data[self.index]["REG"] and self.data[i]["JAM"] == self.data[self.index]["JAM"]:
                jmlA.append(convertToInteger(self.data[i-status]["SUM_ACT_SEC"]))
        return round(sum(jmlA)/len(jmlA))

class Usage(Interpolasi):
    
    def __init__(self,data,index,jam,totalUsage=None,calculateU=None):
        super().__init__(data,index,jam)
        self.totalUsage = totalUsage
        self.calculateU = calculateU
        
    def rumus_kosong(self):
        status = 0
        jmlU = []
        if self.data[self.index-1]["STATUS"] == "UPDATED":
            status = calculate_Count_Update(self.data,self.index) +3
        else:
            status = 3
        for i in range(0,len(self.data)):
            if self.data[i]["REG"] == self.data[self.index]["REG"] and self.data[i]["JAM"] == self.data[self.index]["JAM"] and self.data[i]["WFH_DATE"] == self.data[self.index]["WFH_DATE"]:
                break
            elif self.data[i]["REG"] == self.data[self.index]["REG"] and self.data[i]["JAM"] == self.data[self.index]["JAM"]:
                jmlU.append(convertToInteger(self.data[i-status]["SUM_USAGE"]))
        return round(sum(jmlU)/len(jmlU))

def check(start):
    data = sheet.get_all_records()

    # y=0
    y = data[start]["JAM"]
    count = 1
    for x in range(start,len(data)):
        device = Device(data,x,y)
        activity = Activity(data,x,y)
        usage = Usage(data,x,y)
        interpolasi = Interpolasi(data,x,y)

        try:
            if data[x+1]["KEY"] == "":  #delete row klo ada yang kosong
                print(str(x+3) + " DELETED, Because the row was empty")
                sheet.delete_row(x+3)
        except:
            pass

        if data[x]["JAM"] != y:
            if data[x-1]["STATUS"] == "UPDATED":
                count = count + 1
                sheet.insert_row([interpolasi.makeREG(),y,device.rumus_kosong(),interpolasi.makeWFH(),interpolasi.makeKey(),activity.rumus_kosong(),usage.rumus_kosong(),"UPDATED"],x+2)
            else:
                count = 1
                sheet.insert_row([interpolasi.makeREG(),y,device.rumus_kosong(),interpolasi.makeWFH(),interpolasi.makeKey(),activity.rumus_kosong(),usage.rumus_kosong(),"UPDATED"],x+2)
            print("row: " + str(x+2) + " UPDATED")
            return 1
            
        if y != 23:
            y=y+1
        else:
            y = 0


try:
    while check(start) == 1:
        check(start)

    data = sheet.get_all_records()    
    x = len(data)-1
    interpolasi2 = Interpolasi(data,x,23)
    device2 = Device(data,x,23)
    activity2 = Activity(data,x,23)
    usage2 = Usage(data,x,23)

    if data[x]["JAM"] != 23:                                                                                        #kalo data terakhir tidak di jam 23
        sheet.insert_row([interpolasi2.makeREG(),23,device2.rumus_kosong(),interpolasi2.makeWFH(),interpolasi2.makeKey(),activity2.rumus_kosong(),usage2.rumus_kosong(),"UPDATED"],x+3)
        print("row: " + str(x+3) + " UPDATED")

    print("The Data has been UPDATED\n\n")

    os.system('pause')
except:
    print("Request exceeded by limit!\nPlease try again this app to continue.")
    os.system('pause')