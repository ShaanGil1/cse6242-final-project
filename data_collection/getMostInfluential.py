###This script runs analysis on the dataset to
###find which users tweet the most and which
###users receive the most likes. The returned
###user id's can be converted to usernames by
###using the twitter api or manually with the
###website: https://tweeterid.com/. 
import sqlite3
from sqlite3 import Error
import csv
import pandas as pd

try:
    connection = sqlite3.connect("tweet_DB")
    connection.text_factory = str
except Error as e:
    print("Error occurred: " + str(e))


def build_database():
    create_table_sql = "CREATE TABLE tweets(tweet_id integer, user_id integer, likes integer, compound integer);"
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS tweets;")
    cursor.execute(create_table_sql)
    connection.commit()

    df = pd.read_csv("data_test.csv")  
    print(df["tweet_id"]) 

    count = 0
    for index, row in df.iterrows():
        count += 1
                     
        myQuery = "INSERT INTO tweets VALUES (" + str(row[0]) +"," + "\'" + str(row[8])+ "\'" +"," +str(row[6]) +"," +str(row[19]) +");"
        #print(myQuery)
    
            
            
        cursor = connection.execute(myQuery)
        #val =  cursor.fetchall()[0][0]
        #print(val)
    connection.commit()
    print("end count: ", count)

def find_most_tweets():
    print('finding people who tweet the most')
    print('user_id, num_tweets, avg_sentiment, total_likes')
    sql_statement = "SELECT user_id,COUNT(*), AVG(compound), SUM(likes) FROM tweets GROUP BY user_id ORDER BY 2 DESC LIMIT 50;"
    cursor = connection.execute(sql_statement)
    for line in cursor.fetchall():
        print(line[0], line[1], line[2], line[3])
    

def find_popular():
    print('finding people who receive the most likes')
    print('user_id, num_tweets, avg_sentiment, total_likes')
    sql_statement = "SELECT user_id,COUNT(*), AVG(compound), SUM(likes) FROM tweets GROUP BY user_id ORDER BY 4 DESC LIMIT 50;"
    cursor = connection.execute(sql_statement)
    for line in cursor.fetchall():
        print(line[0], line[1], line[2], line[3])


build_database()
find_most_tweets()
print('')
find_popular()
