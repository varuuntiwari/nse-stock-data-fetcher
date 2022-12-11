import pandas as pd
import store as db

securities_available = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"
bhavcopy = "https://archives.nseindia.com/content/historical/EQUITIES/2022/DEC/cm09DEC2022bhav.csv.zip"

def main(conn):
    # Download and save Securities available for Equity Segment CSV file
    res = pd.read_csv(securities_available)
    db.store_securities(res, 'securities', conn)

    # Download and save bhavcopy CSV file for 9th Dec, 2022
    res = pd.read_csv(bhavcopy)
    db.store_securities(res, 'bhavcopy', conn)

    # Run queries
    query1 = '''SELECT b.SYMBOL, s."NAME OF COMPANY", ((b.CLOSE - b.OPEN)/b.OPEN) AS gain
                FROM bhavcopy b, securities s
                WHERE b.SYMBOL = s.SYMBOL 
                ORDER BY gain DESC LIMIT 25;'''
    result = pd.read_sql_query(query1, conn)
    result.to_csv('query1.csv')
    print('[+] query 1 executed and saved')


if __name__ == "__main__":
    db_name = "database.db"
    conn = db.init_db(db_name)
    main(conn)
    conn.close()