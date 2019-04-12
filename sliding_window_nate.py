import pandas as pd
import sliding_window as sw


class Spike(object):

    def __init__(self, sign, magnitude, birthday):
        self.sign = sign
        self.magnitude = magnitude
        self.birthday = birthday

    def __is_positive__(self):
        return self.sign == True

    def __get_magnitude__(self):
        return self.magnitude

width = 5
window_separation = 10
threshold = .01




def detect_spike(leading, trailing, counter):

    percent_change = (leading - trailing)/trailing
    print(percent_change)
    if percent_change <= -threshold:
        return Spike(False, percent_change, counter)
    elif percent_change >= threshold:
        return Spike(True, percent_change, counter)
    else:
        return None

def get_data(filename, sheetname):
    df = pd.read_excel(filename, sheet_name=sheetname)

    dates = df["date"]
    ticker_list = [ticker for ticker in df.columns[1:]]

    for ticker in ticker_list:
        prices = df[ticker]
        window_trailing = sw.MovingAverage(width)
        window_leading = sw.MovingAverage(width)
        potential_spikes, confirmed_spikes = [], []

        counter = 0
        for price, date in zip(prices, dates):

            # print(price)

            window_leading.__add__(prices[counter+10])
            window_trailing.__add__(price) #|| prices[counter]

            # print("leading shit")
            # print(window_leading.__get__())

            ma_leading = window_leading.__get_ma__()
            ma_trailing = window_trailing.__get_ma__()

            # print("leading, trailing")
            # print(ma_leading, ma_trailing)

            current_spike = detect_spike(ma_leading, ma_trailing, counter)




            if current_spike:
                print("we found one")
                current_sign = current_spike.__is_positive__()
                potential_spikes.append(current_spike)
                for spike in potential_spikes:
                    if current_sign != spike.__is_positive__():
                        confirmed_spikes.append((spike, current_spike))
                        potential_spikes.remove(spike)


            counter += 1

            if counter > 199:
                break

        #test return statement dont keep it here
        return confirmed_spikes

if __name__ == '__main__':
    print(get_data("data/it.xlsx", "Sheet1"))

