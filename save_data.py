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
    app = (row[0])
    category = (row[2])
    ratings = (row[3])
    reviews = (row[4])
    size = (row[5])

    print(app)
    print(category)
    print(ratings)
    print(reviews)
    print(size)

    sql = """insert into data
        (
            app,
            category,
            ratings,
            reviews,
            size
        )
        values
        (%s, %s, %s, %s, %s)
    """

    curs.execute(
        sql,
        (
            app,
            category,
            ratings,
            reviews,
            size
        )
    )

connect.commit()
file.close()
connect.close()
