import pandas as pd
import sys
from error_checks import *


def SaveAndClean(file_name, asset_Dataframe, nasdaq_Dataframe):
    #sava data to excel file
    print('Saving data...')

    file_path = 'data/' + file_name + '.xlsx'
    writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
    
    asset_Dataframe.to_excel(writer, sheet_name='Sheet1')
    nasdaq_Dataframe.to_excel(writer, sheet_name='Sheet2')
    writer.save()

    # clean data
    df_asset = clean(file_path=file_path, sheet_name='Sheet1')
    return df_asset


def clean(file_path, sheet_name):
    dataframe = pd.read_excel(file_path, sheet_name=sheet_name, header=1)
    dataframe = dataframe.drop(dataframe.index[0]) 
    dataframe = dataframe.drop('ticker', axis=1)
    return dataframe


def get_sector_values(sector):
    fin_comps = ['ZION', 'MSFT', 'TRV', 'STI', 'RF', 'PFG', 'MMC', 'KEY', 'JPM', 'STT']
    health_comps = ['ABT', 'BAX', 'BDX', 'CI', 'GILD', 'LH', 'PKI', 'DGX', 'UNH', 'ZBH']
    it_comps = ['XRX', 'TSS', 'SYMC', 'RHT', 'ORCL', 'NTAP', 'HPQ', 'FLIR', 'ADBE', 'CSCO']
    
    if sector == 'financial':
        companies = fin_comps
    elif sector == 'healthcare':
        companies = health_comps
    else:
        companies = it_comps

    begin_date = '1900-1-02'
    end_date = '2018-12-31'
    file_name = sector

    return begin_date, end_date, file_name, companies


# stops the program if custom company has no available data
def dataExists(Dataframe = None, companies = None, saved = None):
    data_results = data_test(Dataframe = Dataframe, companies = companies, saved = saved)    

    failed_result, failed_companies = analyze_results(data_results)

    if failed_result == True:
        print("The test will be stopped because " + str(failed_companies) + " have no data.")
        sys.exit()


# runs test to determine if company has available data
def data_test(Dataframe = None, companies = None, saved = None):
    avail_companies = list(Dataframe)
    if saved == 'no':
        amt = len(companies)
        avail_companies = getComps(amt, avail_companies)
        
    data_tests = monkeyWork(companies, avail_companies)
    return data_tests


# stops the program if data doesn't have required data
def getComps(amount, available_companies):
    possible_companies = []
    try:   
        for i in range(amount):
           possible_companies.append(available_companies[i][1])
        return possible_companies

    except IndexError:
        print("The test will be stopped because the companies have a lack of data.")
        print("Please check the tickers.")
        sys.exit()


# determines if company has data available
def monkeyWork(companies, available_companies):
    data_tests = {}
    for company in companies:
        if company in available_companies:
            data_tests[company] = True
        else:
            data_tests[company] = False
    return data_tests


# analyzes test results to see if any company is missing data
def analyze_results(Tests):
    failed = False
    companies = []
    for company in Tests:
        if Tests.get(company) == False:
            print(company + " has no data.")
            companies.append(company)
            failed = True
    return failed, companies