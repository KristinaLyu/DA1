import pandas as pd
taxi = pd.read_csv('C:/Users/мой компьютер/Downloads/2_taxi_nyc.csv') 

taxi.shape

taxi.dtypes

taxi.head(5)

taxi.columns

taxi = taxi.rename(columns = {'pickup_dt': 'pickup_dt', 
                   'pickup_month': 'pickup_month', 
                   'borough': 'borough', 
                   'pickups': 'pickups', 
                   'hday': 'hday', 
                   'spd': 'spd', 
                   'vsb': 'vsb',
                   'temp': 'temp', 
                   'dewp': 'dewp', 
                   'slp': 'slp', 
                   'pcp 01': 'pcp_01', 
                   'pcp 06': 'pcp_06', 
                   'pcp 24': 'pcp_24', 
                   'sd': 'sd'})

taxi.head(10)

taxi.borough.value_counts()

taxi.pickups.sum()

taxi.groupby('borough')\
        .agg({'pickups': 'sum'})

taxi.groupby('borough').pickups.sum()

min_pickups = taxi.groupby('borough').pickups.sum().idxmin()

taxi.groupby(['borough', 'hday'])\
        .agg({'pickups': 'mean'})

taxi.groupby(['borough', 'hday']).pickups.mean().to_frame()

print(pickups_by_mon_bor)

pickups_by_mon_bor.shape

taxi.temp

def temp_to_celcius(series):
    return (series - 32) * 5 / 9
temp_to_celcius(taxi.temp)  
