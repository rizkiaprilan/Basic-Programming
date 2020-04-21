# def hitung(n):
#     return str(n) + " = " + str(len(n))

# buah = ['apple','bayam','kurma','pisang']
# x = map(hitung,(buah))

# print(list(x)[0])

#=======================================================================================================


# status = 0

# count = 0
# for a in range(0,10):
#     if a%2 == 0:
#         count+=1
#         # return 
    

# status = count
# print(status)

#=======================================================================================================

# import psycopg2
# from pprint import pprint 
# import os

# con = psycopg2.connect(
#     dbname='gis',
#     user='sde',
#     host='gis105-db.udata.id',
#     password='47HAz123',
#     port='5432'
# )

# data = []
# cur = con.cursor()
# query = "select * from dx_telkom_wfh_stg1 where wfh_date != 100 order by wfh_date, reg, jam"
# cur.execute(query)
# rows = cur.fetchall()
    
    
# for r in rows:
#     line= []
#     for i in range(0,6):
#         line.append(int(r[i]))  #masukkan datanya ke variabel data
#         if i==5:
#             line.append(str(r[6]))
#     data.append(line)
# cur.close()

# pprint(data)

#=======================================================================================================

i = int(input('Masukkan angka: '))

def week(i):
    switcher={
           0:'Sunday',
           1:'Monday',
           2:'Tuesday',
           3:'Wednesday',
           4:'Thursday',
           5:'Friday',
           6:'Saturday'
        }
    return switcher.get(i,"Invalid day of week")

print(week(i))