import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)
sheet = client.open("DX_V_TELKOM_WFH Interpolasi2").get_worksheet(1) #mulai dari index 0


# data = sheet.get_all_records()    #data diubah menjadi array
# pprint(data)
#=======================================================================================================
sheet.update_cell(1,5,"STATUS")

start = 0
def check(start):
    data = sheet.get_all_records()

    y = 0
    for x in range(start,len(data)):
    
        if data[x]["JAM"] != y:
            if y==22 and data[x+1]["JAM"] != y+1:
                sheet.insert_row([data[x-1]["REG"],y,round((((data[x-1]["sum_countd_device"]-data[x-2]["sum_countd_device"])*(y-data[x-2]["JAM"]))/(data[x-1]["JAM"]-data[x-2]["JAM"]))+data[x-2]["sum_countd_device"]),data[x-1]["WFH_DATE"],"UPDATED"],x+2)
                print("row: " + str(x+2) + " UPDATED")
            elif y==23 and data[x-1]["STATUS"] == "UPDATED":
                sheet.insert_row([data[x-1]["REG"],y,round((((data[x-2]["sum_countd_device"]-data[x-3]["sum_countd_device"])*(y-data[x-3]["JAM"]))/(data[x-2]["JAM"]-data[x-3]["JAM"]))+data[x-3]["sum_countd_device"]),data[x-1]["WFH_DATE"],"UPDATED"],x+2)
                print("row: " + str(x+2) + " UPDATED")
            elif y==23:
                sheet.insert_row([data[x-1]["REG"],y,round((((data[x-1]["sum_countd_device"]-data[x-2]["sum_countd_device"])*(y-data[x-2]["JAM"]))/(data[x-1]["JAM"]-data[x-2]["JAM"]))+data[x-2]["sum_countd_device"]),data[x-1]["WFH_DATE"],"UPDATED"],x+2)
                print("row: " + str(x+2) + " UPDATED")
            else:
                sheet.insert_row([data[x-1]["REG"],y,round((((data[x+1]["sum_countd_device"]-data[x-1]["sum_countd_device"])*(y-data[x-1]["JAM"]))/(data[x+1]["JAM"]-data[x-1]["JAM"]))+data[x-1]["sum_countd_device"]),data[x-1]["WFH_DATE"],"UPDATED"],x+2)
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
    sheet.insert_row([data[x-1]["REG"],23,round((((data[x-1]["sum_countd_device"]-data[x-2]["sum_countd_device"])*(23-data[x-2]["JAM"]))/(data[x-1]["JAM"]-data[x-2]["JAM"]))+data[x-2]["sum_countd_device"]),data[x-1]["WFH_DATE"],"UPDATED"],x+3)
print("row: " + str(x+3) + " UPDATED")

print("Done")