import psycopg2
import pandas as pd

username = ''
password = ''
database = ''
host = 'localhost'
port = '5432'

data = pd.read_csv(r'C:\Users\user\Desktop\БД\лр3\data.csv')

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

cur1 = conn.cursor()
df = pd.DataFrame(data, columns=['cellphone_id', 'brand', 'model', 'operating system',])



cellphone_id = df['cellphone_id']
brand = df['brand']
model = df['model']
operating_system = df['operating system']


for i, item in df.iteritems():
    unique = item.unique()

for i in range(len(cellphone_id)):
    query1 = """ 
    INSERT INTO cellphones_data(cellphone_id, brand, model, operating_system) VALUES (('%d'), ('%s'), ('%s'), ('%s')) 
    ON CONFLICT (cellphone_id)
    DO NOTHING;
    """ % (cellphone_id[i], brand[i], model[i], operating_system[i])
    cur1.execute(query1)



cur2 = conn.cursor()
df = pd.DataFrame(data, columns=['user_id', 'gender'])

user_id = df['user_id']
gender = df['gender']

for i in range(len(user_id)):
    query2 = """
    INSERT INTO cellphones_users(user_id, gender) VALUES (('%d'), ('%s')) 
    ON CONFLICT (user_id)
    DO NOTHING;
    """ % (user_id[i], gender[i])
    cur2.execute(query2)

conn.commit()


cur3 = conn.cursor()

df = pd.DataFrame(data, columns=['user_id', 'cellphone_id', 'rating'])

user_id = df['user_id']
cellphone_id = df['cellphone_id']
rating = df['rating']

for i in range(len(cellphone_id)):
    query3 = """
    INSERT INTO cellphones_rating(user_id, cellphone_id, rating) VALUES (('%d'), ('%d'), ('%d'));
    """ % (user_id[i], int(cellphone_id[i]), int(rating[i]))
    cur3.execute(query3)

conn.commit()

