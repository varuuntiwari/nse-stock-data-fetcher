import pandas as pd
import store as db

securities_available = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"
bhavcopy = "https://archives.nseindia.com/content/historical/EQUITIES/2022/DEC/cm09DEC2022bhav.csv.zip"

def main(conn):
    res = pd.read_csv(securities_available)
    db.store_securities(res, 'securities', conn)

    res = pd.read_csv(bhavcopy)
    db.store_securities(res, 'bhavcopy', conn)

if __name__ == "__main__":
    db_name = "database.db"
    conn = db.init_db(db_name)
    main(conn)