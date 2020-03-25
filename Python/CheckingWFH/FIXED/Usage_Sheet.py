import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from operator import itemgetter

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)
sheet = client.open("DX_V_TELKOM_WFH Interpolasi2").get_worksheet(5) #mulai dari index 0

# data = sheet.get_all_records()        #data diubah menjadi array
# print(data[len(data)-1]["JAM"])

#=======================================================================================================
sheet.update_cell(1,5,"STATUS")
start = 0

def convertToInteger(stmt):

    if isinstance(stmt,str):                    #kalo dia string
        statementNew = stmt.replace(",","")
        result = int(statementNew) 
    else:
        result = int(stmt)
    return  result

def check(start):

    data = sheet.get_all_records()
    y = 0
    for x in range(start,len(data)):
        if data[x]["JAM"] != y:
            jml = []
            if y==22 and data[x+1]["JAM"] != y+1:
                for i in range(0,len(data)):
                    if data[i]["REG"] == data[x]["REG"] and data[i]["JAM"] == data[x]["JAM"] and data[i]["WFH_DATE"] == data[x]["WFH_DATE"]:
                        break
                    elif data[i]["REG"] == data[x]["REG"] and data[i]["JAM"] == data[x]["JAM"]:
                        jml.append(convertToInteger(data[i-2]["SUM_USAGE"]))

                total = sum(jml)/len(jml)
                sheet.insert_row([data[x-1]["REG"],y,"{:,.0f}".format(round(total)),data[x-1]["WFH_DATE"],"UPDATED"],x+2)
            elif y==23 and data[x-1]["STATUS"] == "UPDATED":
                for i in range(0,len(data)):
                    if data[i]["REG"] == data[x]["REG"] and data[i]["JAM"] == data[x]["JAM"] and data[i]["WFH_DATE"] == data[x]["WFH_DATE"]:
                        break
                    elif data[i]["REG"] == data[x]["REG"] and data[i]["JAM"] == data[x]["JAM"]:
                        jml.append(convertToInteger(data[i-1]["SUM_USAGE"]))

                total = sum(jml)/len(jml)
                sheet.insert_row([data[x-1]["REG"],y,"{:,.0f}".format(round(total)),data[x-1]["WFH_DATE"],"UPDATED"],x+2)
            elif y==23:
                jml  = []
                calculate = (((convertToInteger(data[x-1]["SUM_USAGE"])-convertToInteger(data[x-2]["SUM_USAGE"]))*(y-data[x-2]["JAM"]))/(data[x-1]["JAM"]-data[x-2]["JAM"]))+convertToInteger(data[x-2]["SUM_USAGE"])
                if calculate < 0:
                    for j in range(0,len(data)):
                        if data[j]["REG"] == data[x-1]["REG"] and data[j]["JAM"] == data[x-1]["JAM"] and data[j]["WFH_DATE"]==data[x-1]["WFH_DATE"]:
                            break
                        elif data[j]["REG"] == data[x-1]["REG"] and data[j]["JAM"] == 23:
                            jml.append(convertToInteger(data[j]["SUM_USAGE"]))
                            calculate = sum(jml)/len(jml)
                 
                sheet.insert_row([data[x-1]["REG"],y,"{:,.0f}".format(round(calculate)),data[x-1]["WFH_DATE"],"UPDATED"],x+2)
            else:
                sheet.insert_row([data[x-1]["REG"],y,"{:,.0f}".format(round((((convertToInteger(data[x]["SUM_USAGE"])-convertToInteger(data[x-1]["SUM_USAGE"]))*(y-data[x-1]["JAM"]))/(data[x]["JAM"]-data[x-1]["JAM"]))+convertToInteger(data[x-1]["SUM_USAGE"]))),data[x-1]["WFH_DATE"],"UPDATED"],x+2)
            
            print("row: " + str(x+2) + " UPDATED")
            return 1
            
        if y != 23:
            y=y+1
        else:
            y = 0
        
        if x==len(data):
            return 0

while check(start) == 1:
    check(start)

data = sheet.get_all_records()
x = len(data)-1
if data[x]["JAM"] != 23:
    sheet.insert_row([data[x-1]["REG"],23,"{:,.0f}".format(round((((convertToInteger(data[x-1]["SUM_USAGE"])-convertToInteger(data[x-2]["SUM_USAGE"]))*(23-data[x-2]["JAM"]))/(data[x-1]["JAM"]-data[x-2]["JAM"]))+convertToInteger(data[x-2]["SUM_USAGE"]))),data[x-1]["WFH_DATE"],"UPDATED"],x+3)
print("row: " + str(x+3) + " UPDATED")

print("Done")