import pandas as pd
import sliding_window as sw
import sys


class Spike(object):

    def __init__(self, sign, trailing, magnitude, birthday):
        self.sign = sign
        self.magnitude = magnitude
        self.birthday = birthday
        self.trailing = trailing
        self.confirmed = False

    def __is_positive__(self):
        return self.sign == True

    def __get_magnitude__(self):
        return self.magnitude

width = 5
window_separation = 10
threshold = .1


def detect_spike(leading, trailing, counter):

    percent_change = (leading - trailing)/trailing
    # print(percent_change)
    if percent_change <= -threshold:
        return Spike(False,trailing, percent_change, counter)
    elif percent_change >= threshold:
        return Spike(True, trailing, percent_change, counter)
    else:
        return None

def get_data(filename, sheetname):
    df = pd.read_excel(filename, sheet_name=sheetname)

    dates = df["date"]
    ticker_list = [ticker for ticker in df.columns[1:]]
    ticker = ticker_list[3]
    prices = df[ticker]

    # index into row 10,000
    prices = prices.loc[10000:]

    window_trailing = sw.MovingAverage(width)
    window_leading = sw.MovingAverage(width)
    potential_spikes, spike_list = [], []

    counter = 10000
    for price, date in zip(prices, dates):
        try:
            window_leading.__add__(prices[counter+window_separation])
        except Exception as e:
            break
        window_trailing.__add__(prices[counter])

        # print("leading shit")
        # print(window_leading.__get__())

        ma_leading = window_leading.__get_ma__()
        ma_trailing = window_trailing.__get_ma__()

        # print("leading, trailing")
        # print(ma_leading, ma_trailing)

        current_spike = detect_spike(ma_leading, ma_trailing, counter)


        if current_spike:
            spike_list.append(current_spike)

            # print("we found one")
            current_sign = current_spike.__is_positive__()
            potential_spikes.append(current_spike)

            remove_spike = False

            for spike in potential_spikes:
                if counter - spike.birthday > 30:
                    #print("a spike expired")
                    potential_spikes.remove(spike)

                elif current_sign != spike.__is_positive__():
                    spike.confirmed = True
                    # confirmed_spikes.append((spike, current_spike))
                    potential_spikes.remove(spike)
                    remove_spike = True

            if remove_spike:
                potential_spikes.remove(current_spike)

        counter += 1

        # if counter > 10000:
        #     break

    #test return statement dont keep it here
    # print("potential_spikes", len(potential_spikes))
    for spike in spike_list:
        if spike.confirmed:
            print(spike.birthday)
    return spike_list

def get_key(spike):
    return spike.confirmed


def parse_output(list_of_spikes):
    with open("svm_input.dat", 'w') as outfile:
        list_of_spikes.sort(key=get_key, reverse=True)
        for i in list_of_spikes:
            if i.confirmed:
                outfile.write("1 ")
                outfile.write("1:" + str(i.birthday) + ' 2:'+str(i.magnitude)+' 3:'+str(i.trailing))
            else:
                outfile.write("-1 ")
                outfile.write("1:"+str(i.birthday)+' 2:' + str(i.magnitude)+' 3:'+ str(i.trailing))
            outfile.write("\n")

if __name__ == '__main__':
    huge_list_of_spikes = get_data("data/it.xlsx", "Sheet1")
    parse_output(huge_list_of_spikes)
