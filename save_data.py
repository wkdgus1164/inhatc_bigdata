import csv
import pymysql

connect = pymysql.connect(
    host='bigdata.crjw48i2voq5.ap-northeast-2.rds.amazonaws.com',
    user='root',
    password='Han1353130!',
    db='bigdata',
    charset='utf8',
)

curs = connect.cursor()
connect.commit()

file = open(
    'play-store-apps/googleplaystore.csv',
    'r',
    encoding='UTF-8',
)

csvReader = csv.reader(file)

for row in csvReader:
    rating = row[2]
    reviews = row[3]
    installs = row[5][:-1].replace(',', '')
    type = row[6]
    price = row[7][1:]

    print(rating)
    print(reviews)
    print(installs)
    print(type)
    print(price)

    sql = """insert into data
        (
            rating,
            reviews,
            installs,
            type,
            price
        )
        values
        (%s, %s, %s, %s, %s)
    """

    curs.execute(
        sql,
        (
            rating,
            reviews,
            installs,
            type,
            price
        )
    )

connect.commit()
file.close()
connect.close()
