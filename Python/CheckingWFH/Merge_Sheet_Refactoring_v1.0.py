import gspread 
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import itertools
import threading
import time
import sys

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')
t = threading.Thread(target=animate)
t.start()

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(".\\FIXED\\creds.json",scope)
client = gspread.authorize(creds)
sheet = client.open("DX_V_TELKOM_WFH Interpolasi2").get_worksheet(8) #mulai dari index 0
#=======================================================================================================
sheet.update_cell(1,8,"STATUS")

def convertToInteger(stmt):

    if isinstance(stmt,str):                    #kalo dia string
        statementNew = stmt.replace(",","")
        result = int(statementNew) 
    else:
        result = int(stmt)
    return  result

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

    def rumus_Dempet(self):
        if self.data[self.index-1]["STATUS"] == "UPDATED":
            return round((((self.data[self.index-2]["SUM_COUNTD_DEVICE"]-self.data[self.index-3]["SUM_COUNTD_DEVICE"])*(self.jam-self.data[self.index-3]["JAM"]))/(self.data[self.index-2]["JAM"]-self.data[self.index-3]["JAM"]))+self.data[self.index-3]["SUM_COUNTD_DEVICE"])
        else:
            return round((((self.data[self.index-1]["SUM_COUNTD_DEVICE"]-self.data[self.index-2]["SUM_COUNTD_DEVICE"])*(self.jam-self.data[self.index-2]["JAM"]))/(self.data[self.index-1]["JAM"]-self.data[self.index-2]["JAM"]))+self.data[self.index-2]["SUM_COUNTD_DEVICE"])

    def rumus_Jam_23(self):
        return round((((self.data[self.index-1]["SUM_COUNTD_DEVICE"]-self.data[self.index-2]["SUM_COUNTD_DEVICE"])*(self.jam-self.data[self.index-2]["JAM"]))/(self.data[self.index-1]["JAM"]-self.data[self.index-2]["JAM"]))+self.data[self.index-2]["SUM_COUNTD_DEVICE"])

    def rumus_Jam_23_Terakhir(self):
        return round((((self.data[self.index-1]["SUM_COUNTD_DEVICE"]-self.data[self.index-2]["SUM_COUNTD_DEVICE"])*(23-self.data[self.index-2]["JAM"]))/(self.data[self.index-1]["JAM"]-self.data[self.index-2]["JAM"]))+self.data[self.index-2]["SUM_COUNTD_DEVICE"])

    def rumus_Jam_Kosong(self):
        return round((((self.data[self.index+1]["SUM_COUNTD_DEVICE"]-self.data[self.index-1]["SUM_COUNTD_DEVICE"])*(self.jam-self.data[self.index-1]["JAM"]))/(self.data[self.index+1]["JAM"]-self.data[self.index-1]["JAM"]))+self.data[self.index-1]["SUM_COUNTD_DEVICE"])

class Activity(Interpolasi):
    
    def __init__(self,data,index,jam,totalActivity=None,calculateA=None):
        super().__init__(data,index,jam)
        self.totalActivity = totalActivity
        self.calculateA = calculateA
    
    def rumus_Dempet(self):
        status = 0
        jmlA = []
        if self.data[self.index-1]["STATUS"] == "UPDATED":
            status = 1
        else:
            status = 2
        
        for i in range(0,len(self.data)):
            if self.data[i]["REG"] == self.data[self.index]["REG"] and self.data[i]["JAM"] == self.data[self.index]["JAM"] and self.data[i]["WFH_DATE"] == self.data[self.index]["WFH_DATE"]:
                break
            elif self.data[i]["REG"] == self.data[self.index]["REG"] and self.data[i]["JAM"] == self.data[self.index]["JAM"]:
                jmlA.append(convertToInteger(self.data[i-status]["SUM_ACT_SEC"]))
        return "{:,.0f}".format(round(sum(jmlA)/len(jmlA)))
        # return "{:,.0f}".format(round(self.totalActivity))

    def rumus_Jam_23(self):
        return "{:,.0f}".format(round(self.calculateA))

    def rumus_Jam_23_Terakhir(self):
        return "{:,.0f}".format(round((((convertToInteger(self.data[self.index-1]["SUM_ACT_SEC"])-convertToInteger(self.data[self.index-2]["SUM_ACT_SEC"]))*(23-self.data[self.index-2]["JAM"]))/(self.data[self.index-1]["JAM"]-self.data[self.index-2]["JAM"]))+convertToInteger(self.data[self.index-2]["SUM_ACT_SEC"])))

    def rumus_Jam_Kosong(self):
        return "{:,.0f}".format(round((((convertToInteger(self.data[self.index]["SUM_ACT_SEC"])-convertToInteger(self.data[self.index-1]["SUM_ACT_SEC"]))*(self.jam-self.data[self.index-1]["JAM"]))/(self.data[self.index]["JAM"]-self.data[self.index-1]["JAM"]))+convertToInteger(self.data[self.index-1]["SUM_ACT_SEC"])))

class Usage(Interpolasi):
    
    def __init__(self,data,index,jam,totalUsage=None,calculateU=None):
        super().__init__(data,index,jam)
        self.totalUsage = totalUsage
        self.calculateU = calculateU
    
    def rumus_Dempet(self):
        status = 0
        jmlU = []
        if self.data[self.index-1]["STATUS"] == "UPDATED":
            status = 1
        else:
            status = 2
        for i in range(0,len(self.data)):
            if self.data[i]["REG"] == self.data[self.index]["REG"] and self.data[i]["JAM"] == self.data[self.index]["JAM"] and self.data[i]["WFH_DATE"] == self.data[self.index]["WFH_DATE"]:
                break
            elif self.data[i]["REG"] == self.data[self.index]["REG"] and self.data[i]["JAM"] == self.data[self.index]["JAM"]:
                jmlU.append(convertToInteger(self.data[i-status]["SUM_USAGE"]))
        
        return "{:,.0f}".format(round(sum(jmlU)/len(jmlU)))

        # return "{:,.0f}".format(round(self.totalUsage))

    def rumus_Jam_23(self):
        return "{:,.0f}".format(round(self.calculateU))

    def rumus_Jam_23_Terakhir(self):
        return "{:,.0f}".format(round((((convertToInteger(self.data[self.index-1]["SUM_USAGE"])-convertToInteger(self.data[self.index-2]["SUM_USAGE"]))*(23-self.data[self.index-2]["JAM"]))/(self.data[self.index-1]["JAM"]-self.data[self.index-2]["JAM"]))+convertToInteger(self.data[self.index-2]["SUM_USAGE"])))

    def rumus_Jam_Kosong(self):
        return "{:,.0f}".format(round((((convertToInteger(self.data[self.index]["SUM_USAGE"])-convertToInteger(self.data[self.index-1]["SUM_USAGE"]))*(self.jam-self.data[self.index-1]["JAM"]))/(self.data[self.index]["JAM"]-self.data[self.index-1]["JAM"]))+convertToInteger(self.data[self.index-1]["SUM_USAGE"])))

def check(start):
    data = sheet.get_all_records()

    y = 0
    for x in range(start,len(data)):
        device = Device(data,x,y)
        activity = Activity(data,x,y)
        usage = Usage(data,x,y)
        interpolasi = Interpolasi(data,x,y)

        try:
            if data[x+1]["KEY"] == "":  #delete row klo ada yang kosong
                sheet.delete_row(x+3)
        except:
            pass

        jmlA = []
        jmlU = []
        if data[x]["JAM"] != y:
            if int(abs(data[x-1]["JAM"] - data[x]["JAM"])) >= 3 and int(abs(data[x-1]["JAM"] - data[x]["JAM"])) < 23:     #klo ada data jam yang kosong berdempetan
                if data[x-1]["STATUS"] == "UPDATED":

                    sheet.insert_row([interpolasi.makeREG(),y,device.rumus_Dempet(),interpolasi.makeWFH(),interpolasi.makeKey(),activity.rumus_Dempet(),usage.rumus_Dempet(),"UPDATED"],x+2)
                else:

                    sheet.insert_row([interpolasi.makeREG(),y,device.rumus_Dempet(),interpolasi.makeWFH(),interpolasi.makeKey(),activity.rumus_Dempet(),usage.rumus_Dempet(),"UPDATED"],x+2)
            elif y==23:                                                                                         #klo data yang kosong di jam 23
                calculateA = (((convertToInteger(data[x-1]["SUM_ACT_SEC"])-convertToInteger(data[x-2]["SUM_ACT_SEC"]))*(y-data[x-2]["JAM"]))/(data[x-1]["JAM"]-data[x-2]["JAM"]))+convertToInteger(data[x-2]["SUM_ACT_SEC"])
                calculateU = (((convertToInteger(data[x-1]["SUM_USAGE"])-convertToInteger(data[x-2]["SUM_USAGE"]))*(y-data[x-2]["JAM"]))/(data[x-1]["JAM"]-data[x-2]["JAM"]))+convertToInteger(data[x-2]["SUM_USAGE"])
                if calculateA < 0:
                    for j in range(0,len(data)):
                        if data[j]["REG"] == data[x-1]["REG"] and data[j]["JAM"] == data[x-1]["JAM"] and data[j]["WFH_DATE"]==data[x-1]["WFH_DATE"]:
                            break
                        elif data[j]["REG"] == data[x-1]["REG"] and data[j]["JAM"] == 23:
                            jmlA.append(convertToInteger(data[j]["SUM_ACT_SEC"]))
                            calculateA_ = sum(jmlA)/len(jmlA)
                            
                            activity23 = Activity(data,x,y,calculateA=calculateA_)

                if calculateU < 0:
                    for j in range(0,len(data)):
                        if data[j]["REG"] == data[x-1]["REG"] and data[j]["JAM"] == data[x-1]["JAM"] and data[j]["WFH_DATE"]==data[x-1]["WFH_DATE"]:
                            break
                        elif data[j]["REG"] == data[x-1]["REG"] and data[j]["JAM"] == 23:
                            jmlU.append(convertToInteger(data[j]["SUM_USAGE"]))
                            calculateU_ = sum(jmlU)/len(jmlU)

                            usage23 = Usage(data,x,y,calculateU=calculateU_)

                sheet.insert_row([interpolasi.makeREG(),y,device.rumus_Jam_23(),interpolasi.makeWFH(),interpolasi.makeKey(),activity23.rumus_Jam_23(),usage23.rumus_Jam_23(),"UPDATED"],x+2)
            else:                                                                                               #klo data jam yang kosong cuman 1

                sheet.insert_row([interpolasi.makeREG(),y,device.rumus_Jam_Kosong(),interpolasi.makeWFH(),interpolasi.makeKey(),activity.rumus_Jam_Kosong(),usage.rumus_Jam_Kosong(),"UPDATED"],x+2)
            
            # print("row: " + str(x+2) + " UPDATED")
            return 1
            
        if y != 23:
            y=y+1
        else:
            y = 0

start = 0
while check(start) == 1:
    check(start)

data = sheet.get_all_records()
x = len(data)-1
interpolasi2 = Interpolasi(data,x,23)
device2 = Device(data,x,23)
activity2 = Activity(data,x,23)
usage2 = Usage(data,x,23)

if data[x]["JAM"] != 23:                                                                                        #kalo data terakhir tidak di jam 23
    sheet.insert_row([interpolasi2.makeREG(),23,device2.rumus_Jam_23_Terakhir(),interpolasi2.makeWFH(),interpolasi2.makeKey(),activity2.rumus_Jam_23_Terakhir(),usage2.rumus_Jam_23_Terakhir(),"UPDATED"],x+3)
    # print("row: " + str(x+3) + " UPDATED")

done = True