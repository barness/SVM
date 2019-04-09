import pandas as pd
import sliding_window as sw

width = 5
window_separation = 14


def get_data(filename, sheetname):
    df = pd.read_excel(filename, sheet_name=sheetname)

    dates = df["date"]
    ticker_list = [ticker for ticker in df.columns[1:]]

    for ticker in ticker_list:
        prices = df[ticker]
        window_trailing = sw.MovingAverage(width)
        window_leading = sw.MovingAverage(width)

        for price in prices:
            price


    return ticker_list

def parse_data(list_of_tickers):
    pass


if __name__ == '__main__':
    big_list_of_tickers = get_data("it.xlsx", "Sheet1")
    big_output = parse_data(big_list_of_tickers)
