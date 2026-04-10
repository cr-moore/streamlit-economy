from config.series_map import series_dict
import requests
import pandas as pd

def get_data():
    # create request
    series_ids = [] 
    for key, value in series_dict.items():
        series_ids.append(key)

    payload = {"seriesid": series_ids}
    url = "https://api.bls.gov/publicAPI/v1/timeseries/data/"


    # get data
    response = requests.get(url, json=payload)

    data = response.json()
    data_results = data['Results']['series']

    # create data frame
    df = pd.DataFrame()

    for series_index in range(len(data_results)):
        # clean data
        df2 = pd.DataFrame(data_results[series_index]['data'])
        df2 = df2.drop(['footnotes'], axis=1)
        df2 = df2.drop(['period'], axis=1)
        df2 = df2.drop(['latest'], axis=1)
        df2['month'] = df2['periodName']
        df2 = df2.drop(['periodName'], axis=1)
        df2['item'] = series_dict[data_results[series_index]['seriesID']]['name']
        df2['unit'] = series_dict[data_results[series_index]['seriesID']]['unit']
        df2['date'] = pd.to_datetime(df2['year'].astype(str) + ' ' + df2['month'], format='%Y %B')
        df2['value'] = pd.to_numeric(df2['value'], errors='coerce')

        # concat data frame
        df = pd.concat([df, df2], ignore_index=True)

    df = df.sort_values('date')
    #cache data in excel
    df.to_csv('datafolder/cpi_data.csv', index=False)