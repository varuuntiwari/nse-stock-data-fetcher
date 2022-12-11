# nse-stock-data-fetcher
script to fetch stock data and run SQL queries on it

# Question
NSE stock data fetcher + query

Acquire Data:

1. Programmatically fetch “Securities available for Equity segment (.csv)” file From the URL: https://www.nseindia.com/market-data/securities-available-for-trading
2. Programatically get the latest “bhavcopy” csv file from the following URL - https://www.nseindia.com/all-reports
3. Construct a (relational) database with normalized tables & insert both the data files into it
4. In addition to step 2, programmatically get bhav copies of the last 30 days instead of just the latest one.

Queries:

1. Write a SQL query to fetch the top 25 gainers of the day sorted in the order of their gains. Gains is defined as [(close - open) / open] for the day concerned as per point 2 above.
2. Get date wise top 25 gainers for the last 30 days as per point 4 above.
3. Get a single list of top 25 gainers using the open of the oldest day and close of the latest day of those 30 days as per point 4.

Rules of the game:

Code must be written in python & SQL queries wherever applicable. Jupyter notebooks must not be submitted in the final code, instead proper python / SQL code files must be submitted. You can use any open source tools / libraries to complete this task as required.

The assignment has to be completed today. After the assignment is complete, send us the github link to the code along with output csv files from all queries. Your output must have all the required data required to understand it. Code quality matters to us.

If you have any other questions, you can reach out to us here. All the best!

# Usage
1. Run the command `.\venv\Scripts\activate` to start virtual environment.
2. Run `pip install -r requirements.txt` to install required libraries.
3. Run `python app.py` to write query outputs in CSV files.