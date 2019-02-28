import data_collect
import data_utils as data_utils
import custom_utils as utils
from error_checks import *


# runs custom mode
def Custom(rerun_count):

    #check if function has ran before so this doesnt keep getting printed out
    if rerun_count == 0:
        print("\n---CUSTOM MODE---")
    
    #verify input
    amt = int_check('Enter how many companies are in your portfolio: ', min_num = 0)    

    #gets symbols and stores in a list
    tickers = utils.get_symbols(amt)

    #get dates
    begin_date, end_date = utils.get_dates()

    #ask if the user wants to save the historical data of each company
    file_name = input("Please Enter a file name for the performances: ")

    # pull data
    trash = data_collect.pull(companies = tickers, begin_date = begin_date, end_date = end_date, file_name = file_name)
    df_asset, df_nasdaq, companies = data_collect.get_file(file_name)


# runs sector mode 
def Sectors(rerun_count):
    sectors = 'financial,healthcare,it'
    
    # get proper sector
    if rerun_count == 0:
        print("Please select from one of the following sectors: Financial,Healthcare,IT\n")
    sector = str_verify("I choose sector(financial, healthcare, it): ", sectors, lower = "yeet")

    begin_date, end_date, file_name, companies = data_utils.get_sector_values(sector)
    df_asset, df_nasdaq, companies = data_collect.get_file(file_name)