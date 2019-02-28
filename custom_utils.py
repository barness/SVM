from error_checks import *

def get_symbols(amt_tickers):
    tickers = []
    for i in range (1, amt_tickers+1):
        symbol = input("Enter the tickers of company " + str(i) + ": ").upper().replace(" ", '')
        #error check input && ASK PROFESSOR PARK ABOUT REQUIREMENTS ON SYMBOLS
        while not ticker_verify(symbol): 
            symbol = input("Invalid symbol. Enter the tickers of company " + str(i) + ": ").upper().replace(" ", '')
        tickers.append(symbol)
    print("\nThe tickers are: " + str(tickers))

        #determine if editing is required
    ans = str_verify("Edit any of the tickers (Y/N): ", "y,n", lower = 'yeet')
    if ans == 'y':
        tickers = editSymbols(ans, tickers)

    return tickers

def editSymbols(answer, tickers):

    #edit tickers
    while answer == 'y':
        
        #verify input
        position = int_check('Which company number would you like to edit: ', min_num = 1, max_num = len(tickers))
        new_symbol = input('Please enter new ticker for company ' + str(position) + ": ").upper()
        while not ticker_verify(new_symbol):
            new_symbol = input('Invalid input. Please enter new ticker for company ' + str(position) + ": ").upper()
        tickers[position - 1] = new_symbol
        print("\nThe tickers are now: " + str(tickers))
        
        answer = str_verify("Edit any of the tickers (Y/N): ", "y,n", lower = "yeet")

    return tickers


def editDates(answer, begin_date, end_date):
    while answer == 'y':
        date = str_verify('Which date would you like to edit (begin, end): ', "begin,end", lower = 'yeet')
        if date == 'begin':
            begin_date = getDate()
        else:
            end_date = getDate('end')
        print("\nThe beginning date is " + begin_date + " and the end date is " + end_date)
        answer = str_verify("Edit any of the dates (Y/N): ", "y,n", lower = 'yeet')
    return begin_date, end_date

# runs interface to prompt user for dates
def get_dates():
    # get dates
    print("\nA time window must be specified to generate the portfolios")
    begin_date = getDate()
    end_date = getDate('end')

    print("\nThe program will analyze data from " + begin_date + " to " + end_date)
    
    # edit any of the dates
    ans = str_verify("Edit any of the dates (Y/N): ", "y,n", lower = 'yeet')
    if ans == 'y':
        begin_date, end_date = editDates(ans, begin_date, end_date)    
    
    # make sure the dates are entered in the correct order, if not switch them
    begin_date, end_date = datesTest(begin_date, end_date)

    return begin_date, end_date


def getDate(*args):
    if len(args) == 0:
        word = "from"
        newline = ''
    else:
        word = 'to'
        newline = '\n'
    
    year = str(int_check(newline + "Please enter the year you'd like the program to analyze " + word + ": ", max_num = 2018, min_num = 1965))
    month = str(int_check("Please enter the month: ", min_num = 1, max_num = 12))
    day = str(int_check("Please enter the day: ", min_num = 1, max_num = 32))
    
    if len(day) == 1:
        day = '0' + day

    date = year + '-' + month + '-' + day
    
    return date

def datesTest(begin_date, end_date):
    begin_dates = begin_date.split('-')
    end_dates = end_date.split('-')
    
    if int(begin_dates[0]) > int(end_dates[0]):
        begin_date, end_date = switcheroo(begin_date, end_date) 

    elif int(begin_dates[0]) == int(end_dates[0]) and int(begin_dates[1]) > int(end_dates[1]):
        begin_date, end_date = switcheroo(begin_date, end_date)

    elif int(begin_dates[0]) == int(end_dates[0]) and int(begin_dates[1]) == int(end_dates[1]) and int(begin_dates[2]) > int(end_dates[2]):
        begin_date, end_date = switcheroo(begin_date, end_date)

    return begin_date, end_date

def switcheroo(begin_date, end_date):
    temp = begin_date
    begin_date = end_date
    end_date = temp

    print("\nThe program automatically switched the dates.")
    print("The beginning date is " + begin_date  + " and the end date is " + end_date)
    
    return begin_date, end_date

# get desired techinques from the user
def getTechniques():
    print("\nEnter any of the following techniques you'd like to run:\n\tMarkowitz\n\tTreynor-Black(Treynor)")
    techs = str_verify("\nEnter the techniques you'd like to run, separated by a comma: ", "markowitz,treynor", lower = 'yeet', multiple = 'yeet')
    
    return techs

def ticker_verify(ticker):
    if len(ticker) > 5:
        return False
    return True