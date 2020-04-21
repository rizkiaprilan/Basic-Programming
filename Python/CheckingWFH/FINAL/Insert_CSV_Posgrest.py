import csv
from pprint import pprint
import psycopg2

con = psycopg2.connect(
    dbname='gis',
    user='sde',
    host='gis105-db.udata.id',
    password='47HAz123',
    port='5432'
)

with open("CSV/dx_telkom_wfh_20200330_1.csv") as csv_file:          ##PENTING!!!
    cur = con.cursor()
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # data = []
    for row in csv_reader:
        # print(row)
        if line_count == 0:
            line_count += 1
        else:
            # data.append(row)
            cur.execute("""INSERT INTO dx_telkom_wfh_stg1 (reg,jam,sum_countd_device,wfh_date,sum_act_sec,sum_usage,status) VALUES (%s, %s, %s, %s, %s, %s, %s);""",(row[0], row[1], row[2],row[3],row[4],row[5],None)) ##PENTING!!!
            line_count += 1
            con.commit()
        
    print('DATA INSERTED')
    cur.close()
    con.close()

    

