import sqlite3

def doesTableExist(): 
    conn = sqlite3.connect('tweet_example.db')
    cur = conn.cursor()

    table_exist_query = ''' SELECT count(*) FROM sqlite_master WHERE type='table' AND name='tweet_info' '''
    cur.execute(table_exist_query)
    exist_result = cur.fetchone()

    if exist_result[0]==1:
        print("tweet_info table exists.")
    else:
        print("tweet_info table does not exist.")
    conn.close()