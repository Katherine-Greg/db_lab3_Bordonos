import psycopg2
import matplotlib.pyplot as plt

username = ''
password = ''
database = ''
host = 'localhost'
port = '5432'

query1 = '''
SELECT brand, COUNT(cellphones_rating.cellphone_id) AS Amount
FROM cellphones_data
INNER JOIN cellphones_rating
ON cellphones_data.cellphone_id = cellphones_rating.cellphone_id
GROUP BY cellphones_data.brand
'''

query2 = '''
SELECT model, AVG(rating) AS Rating
FROM cellphones_data
INNER JOIN cellphones_rating
ON cellphones_data.cellphone_id = cellphones_rating.cellphone_id
GROUP BY cellphones_data.model
'''

query3 = '''
SELECT gender, COUNT(gender) AS Amount FROM cellphones_users
GROUP BY gender
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur1 = conn.cursor()
    cur1.execute(query1)
    brand = []
    b_amount = []

    for i in cur1:
        brand.append(i[0])
        b_amount.append(i[1])

    for i in range(len(brand)):
        print(brand[i], '  ', b_amount[i])
    
    print('\n')

    
    cur2 = conn.cursor()
    cur2.execute(query2)
    models = []
    rating = []

    for i in cur2:
        models.append(i[0])
        rating.append(i[1])

    for i in range(len(models)):
        print(models[i], '  ', rating[i])

    print('\n')


    cur3 = conn.cursor()
    cur3.execute(query3)
    gender = []
    g_amount = []

    for i in cur3:
        gender.append(i[0])
        g_amount.append(i[1])

    for i in range(len(gender)):
        print(gender[i], '  ', g_amount[i])
    
    print('\n')


x = [i for i in range(len(brand))]

plt.figure(figsize=(6 ,7))
bar = plt.bar(x, b_amount, width=0.5)
plt.title('Популярність брендів смартфонів за кількістю користувачів')
plt.xlabel('Бренд')
plt.tick_params(axis = 'x', which = 'major', labelsize = 10, color = 'm', labeltop = True, labelbottom = False, labelrotation = 90)
plt.xticks(x, brand)
plt.ylabel('Рейтинг')
plt.tight_layout()
plt.show()


plt.pie(g_amount, labels=gender, autopct='%1.1f%%')
plt.title('Частка гендерів користувачів')
plt.show()


x = [i for i in range(len(models))]
plt.figure(figsize=(6 ,7))
bar = plt.bar(x, rating, width=0.5)
plt.title('Рейтинг брендів смартфонів за відгуками користувачів')
plt.xlabel('Бренд')
plt.tick_params(axis = 'x', which = 'major', labelsize = 10, color = 'm', labeltop = True, labelbottom = False, labelrotation = 90)
plt.xticks(x, models)
plt.ylabel('Рейтинг')
plt.tight_layout()
plt.show()
