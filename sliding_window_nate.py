import pandas as pd
import sliding_window as sw

width = 5
window_separation = 10
threshold = .1


def get_magnitude(leading, trailing):
    pass
    #sam will write this




def get_data(filename, sheetname):
    df = pd.read_excel(filename, sheet_name=sheetname)

    dates = df["date"]
    ticker_list = [ticker for ticker in df.columns[1:]]

    for ticker in ticker_list:
        prices = df[ticker]
        window_trailing = sw.MovingAverage(width)
        window_leading = sw.MovingAverage(width)

        counter = 0
        for price, date in zip(prices, dates):
            window_leading.__add__(prices[counter+10])
            window_trailing.__add__(price) #|| prices[counter]

            ma_leading = window_leading.__get_ma__()
            ma_trailing = window_trailing.__get_ma__()

            if get_magnitude(ma_leading, ma_trailing) > threshold:
                #record_features() - sam will write this also

            counter += 1




    return ticker_list

def parse_data(list_of_tickers):
    pass


if __name__ == '__main__':
    big_list_of_tickers = get_data("it.xlsx", "Sheet1")
    big_output = parse_data(big_list_of_tickers)
