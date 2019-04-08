import pandas as pd

def get_data(filename, sheetname):
    
    df = pd.read_excel(filename, sheet_name = sheetname)
    
    ticker_list = [ticker for ticker in df.columns[1:]]

    dates = df["date"]


    for ticker in ticker_list:
    	
    	prices = df[ticker]

    # 

    # 

    return ticker_list

def parse_data(list_of_tickers):


if __name__ == '__main__':
    big_list_of_tickers = get_data("it.xlsx", "Sheet1")
    big_output = parse_data(big_list_of_tickers)
