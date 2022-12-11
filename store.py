import sqlite3 as sql

def init_db(db_name):
    try:
        conn = sql.connect(db_name)
        print('[+] connected to db')
    except sql.Error as err:
        print('[-] error connecting: ', err)
    finally:
        return conn

def store_securities(df, table_name, conn):
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.commit()
    print(f'[+] wrote {len(df.index)} rows to table `{table_name}`')