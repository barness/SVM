import sys
import quandl
import pandas as pd
import xlrd
import data_utils as utils


def pull(sector = None, companies = None, begin_date = None, end_date = None, file_name = None):
    quandl.ApiConfig.api_key = 'oy3X69-yWwcwM_9HRNbE'
    asset_columns = ['ticker', 'date', 'adj_close']
    nasdaq_columns = ['Trade Date', "Index Value"]
    
    # Let user know
    print('\nPulling data...')

    #Sector values
    if sector is not None:
        begin_date, end_date, file_name, companies = utils.get_sector_values(sector = sector)
            
        df_asset = asset_data_collect(companies=companies, begin_date=begin_date, end_date=end_date, columns=asset_columns)
        df_nasdaq = nasdaq_data_collect(begin_date=begin_date, end_date=end_date, columns=nasdaq_columns)

        df_asset = utils.SaveAndClean(file_name=file_name, asset_Dataframe=df_asset, nasdaq_Dataframe=df_nasdaq)

        return df_asset, df_nasdaq, begin_date, end_date

    # Custom Values
    else:
        #Collect the data from Quandl
        df_asset = asset_data_collect(companies = companies, begin_date = begin_date, end_date = end_date, columns = asset_columns)
        df_nasdaq = nasdaq_data_collect(begin_date = begin_date, end_date = end_date, columns = nasdaq_columns)
             
        #Save and clean the data
        df_asset = utils.SaveAndClean(file_name = file_name, asset_Dataframe = df_asset, nasdaq_Dataframe = df_nasdaq)

        #Examine if data exists
        print('Examining data...')
        utils.dataExists(Dataframe = df_asset, companies = companies)

        print('Data is prepared...')
        return df_asset, df_nasdaq


def get_file(sector):
    file_path = 'data/' + sector + '.xlsx'
    asset_sheet = 'Sheet1'
    nasdaq_sheet = 'Sheet2'
    
    try:
        df_asset = utils.clean(file_path, asset_sheet)

        df_nasdaq = pd.read_excel(file_path, sheet_name=nasdaq_sheet, header=0)
        df_nasdaq = df_nasdaq["Index Value"]

    except (Exception) as e:
        df_asset, df_nasdaq, begin_date, end_date = pull(sector = sector)

    companies = [company for company in df_asset.columns]

    return df_asset, df_nasdaq, companies


def nasdaq_data_collect(begin_date = None, end_date = None, columns = None):
    r_data = quandl.get("NASDAQOMX/COMP", qopts = {'columns' : columns},
        date={'gte':begin_date, 'lte':end_date}, paginate=True)

    df = r_data.loc[begin_date:end_date]
    df = df["Index Value"]

    return df


def asset_data_collect(companies = None, begin_date = None, end_date = None, columns = None):
    #pull data
    r_data = quandl.get_table('WIKI/PRICES', ticker=companies, qopts={'columns': columns},
        date={'gte':begin_date, 'lte':end_date}, paginate=True)
    index_data = r_data.set_index('date')
    df = index_data.pivot(columns='ticker')
    return df


def get_sector_dates():
    return '1900-1-02', '2019-4-20'