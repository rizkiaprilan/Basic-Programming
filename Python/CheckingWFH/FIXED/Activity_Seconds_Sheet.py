import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)
sheet = client.open("DX_V_TELKOM_WFH Interpolasi2").get_worksheet(3) #mulai dari index 0

# data = sheet.get_all_records()    #data diubah menjadi array
# print(data)

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
            y = []
            if y==22 and data[x+1]["JAM"] != y+1:
                for i in range(0,len(data)):
                    if data[i]["REG"] == data[x]["REG"] and data[i]["JAM"] == data[x]["JAM"] and data[i]["WFH_DATE"] == data[x]["WFH_DATE"]:
                        break
                    elif data[i]["REG"] == data[x]["REG"] and data[i]["JAM"] == data[x]["JAM"]:
                        jml.append(convertToInteger(data[i-2]["SUM_ACT_SEC"]))

                total = sum(jml)/len(jml)
                sheet.insert_row([data[x-1]["REG"],y,"{:,.0f}".format(round(total)),data[x-1]["WFH_DATE"],"UPDATED"],x+2)
            elif y==23 and data[x-1]["STATUS"] == "UPDATED":
                for i in range(0,len(data)):
                    if data[i]["REG"] == data[x]["REG"] and data[i]["JAM"] == data[x]["JAM"] and data[i]["WFH_DATE"] == data[x]["WFH_DATE"]:
                        break
                    elif data[i]["REG"] == data[x]["REG"] and data[i]["JAM"] == data[x]["JAM"]:
                        jml.append(convertToInteger(data[i-1]["SUM_ACT_SEC"]))

                total = sum(jml)/len(jml)
                sheet.insert_row([data[x-1]["REG"],y,"{:,.0f}".format(round(total)),data[x-1]["WFH_DATE"],"UPDATED"],x+2)
            elif y==23:
                jml  = []
                calculate = (((convertToInteger(data[x-1]["SUM_ACT_SEC"])-convertToInteger(data[x-2]["SUM_ACT_SEC"]))*(y-data[x-2]["JAM"]))/(data[x-1]["JAM"]-data[x-2]["JAM"]))+convertToInteger(data[x-2]["SUM_ACT_SEC"])

                print("Calculate Before: " + str(calculate))
                print("x: " + str(y), " x1: " + str(data[x-2]["JAM"]), " x2: " + str(data[x-1]["JAM"]), " y1: " + str(data[x-2]["SUM_ACT_SEC"]), " y2: " + str(data[x-1]["SUM_ACT_SEC"]),)

                
                if calculate < 0:
                    for j in range(0,len(data)):
                        if data[j]["REG"] == data[x-1]["REG"] and data[j]["JAM"] == data[x-1]["JAM"] and data[j]["WFH_DATE"]==data[x-1]["WFH_DATE"]:
                            break
                        elif data[j]["REG"] == data[x-1]["REG"] and data[j]["JAM"] == 23:
                            jml.append(convertToInteger(data[j]["SUM_ACT_SEC"]))
                            calculate = sum(jml)/len(jml)
                
                print("Calculate After: " + str(calculate))
                # print("x: " + str(y), " x1: " + str(data[x-1]["JAM"]), " x2: " + str(data[x]["JAM"]), " y1: " + str(data[x-1]["SUM_ACT_SEC"]), " y2: " + str(data[x]["SUM_ACT_SEC"]),)


                sheet.insert_row([data[x-1]["REG"],y,"{:,.0f}".format(round(calculate)),data[x-1]["WFH_DATE"],"UPDATED"],x+2)
            else:
                # print("x: " + str(y), " x1: " + str(data[x-1]["JAM"]), " x2: " + str(data[x]["JAM"]), " y1: " + str(data[x-1]["SUM_ACT_SEC"]), " y2: " + str(data[x]["SUM_ACT_SEC"]),)

                sheet.insert_row([data[x-1]["REG"],y,"{:,.0f}".format(round((((convertToInteger(data[x]["SUM_ACT_SEC"])-convertToInteger(data[x-1]["SUM_ACT_SEC"]))*(y-data[x-1]["JAM"]))/(data[x]["JAM"]-data[x-1]["JAM"]))+convertToInteger(data[x-1]["SUM_ACT_SEC"]))),data[x-1]["WFH_DATE"],"UPDATED"],x+2)

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
    sheet.insert_row([data[x-1]["REG"],23,"{:,.0f}".format(round((((convertToInteger(data[x-1]["SUM_ACT_SEC"])-convertToInteger(data[x-2]["SUM_ACT_SEC"]))*(23-data[x-2]["JAM"]))/(data[x-1]["JAM"]-data[x-2]["JAM"]))+convertToInteger(data[x-2]["SUM_ACT_SEC"]))),data[x-1]["WFH_DATE"],"UPDATED"],x+3)
print("row: " + str(x+3) + " UPDATED")

# print("x: " + str(23), " x1: " + str(data[x-2]["JAM"]), " x2: " + str(data[x-1]["JAM"]), " y1: " + str(data[x-2]["SUM_ACT_SEC"]), " y2: " + str(data[x-1]["SUM_ACT_SEC"]),)


print("Done")