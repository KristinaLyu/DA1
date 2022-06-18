```python
import pandas as pd
taxi = pd.read_csv('C:/Users/мой компьютер/~')
```


```python
import pandas as pd
taxi = pd.read_csv('C:/Users/мой компьютер/Downloads/2_taxi_nyc.csv')
```


```python
taxi.shape
```




    (29101, 14)




```python
taxi.dtypes
```




    pickup_dt        object
    pickup_month     object
    borough          object
    pickups           int64
    hday             object
    spd             float64
    vsb             float64
    temp            float64
    dewp            float64
    slp             float64
    pcp 01          float64
    pcp 06          float64
    pcp 24          float64
    sd              float64
    dtype: object




```python
taxi.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pickup_dt</th>
      <th>pickup_month</th>
      <th>borough</th>
      <th>pickups</th>
      <th>hday</th>
      <th>spd</th>
      <th>vsb</th>
      <th>temp</th>
      <th>dewp</th>
      <th>slp</th>
      <th>pcp_01</th>
      <th>pcp_06</th>
      <th>pcp_24</th>
      <th>sd</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015-01-01 01:00:00</td>
      <td>Jan</td>
      <td>Bronx</td>
      <td>152</td>
      <td>Y</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>30.0</td>
      <td>7.0</td>
      <td>1023.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015-01-01 01:00:00</td>
      <td>Jan</td>
      <td>Brooklyn</td>
      <td>1519</td>
      <td>Y</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>30.0</td>
      <td>7.0</td>
      <td>1023.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015-01-01 01:00:00</td>
      <td>Jan</td>
      <td>EWR</td>
      <td>0</td>
      <td>Y</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>30.0</td>
      <td>7.0</td>
      <td>1023.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015-01-01 01:00:00</td>
      <td>Jan</td>
      <td>Manhattan</td>
      <td>5258</td>
      <td>Y</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>30.0</td>
      <td>7.0</td>
      <td>1023.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015-01-01 01:00:00</td>
      <td>Jan</td>
      <td>Queens</td>
      <td>405</td>
      <td>Y</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>30.0</td>
      <td>7.0</td>
      <td>1023.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
taxi.columns
```




    Index(['pickup_dt', 'pickup_month', 'borough', 'pickups', 'hday', 'spd', 'vsb',
           'temp', 'dewp', 'slp', 'pcp 01', 'pcp 06', 'pcp 24', 'sd'],
          dtype='object')




```python
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
```


```python
taxi.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pickup_dt</th>
      <th>pickup_month</th>
      <th>borough</th>
      <th>pickups</th>
      <th>hday</th>
      <th>spd</th>
      <th>vsb</th>
      <th>temp</th>
      <th>dewp</th>
      <th>slp</th>
      <th>pcp_01</th>
      <th>pcp_06</th>
      <th>pcp_24</th>
      <th>sd</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015-01-01 01:00:00</td>
      <td>Jan</td>
      <td>Bronx</td>
      <td>152</td>
      <td>Y</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>30.0</td>
      <td>7.0</td>
      <td>1023.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015-01-01 01:00:00</td>
      <td>Jan</td>
      <td>Brooklyn</td>
      <td>1519</td>
      <td>Y</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>30.0</td>
      <td>7.0</td>
      <td>1023.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015-01-01 01:00:00</td>
      <td>Jan</td>
      <td>EWR</td>
      <td>0</td>
      <td>Y</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>30.0</td>
      <td>7.0</td>
      <td>1023.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015-01-01 01:00:00</td>
      <td>Jan</td>
      <td>Manhattan</td>
      <td>5258</td>
      <td>Y</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>30.0</td>
      <td>7.0</td>
      <td>1023.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015-01-01 01:00:00</td>
      <td>Jan</td>
      <td>Queens</td>
      <td>405</td>
      <td>Y</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>30.0</td>
      <td>7.0</td>
      <td>1023.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2015-01-01 01:00:00</td>
      <td>Jan</td>
      <td>Staten Island</td>
      <td>6</td>
      <td>Y</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>30.0</td>
      <td>7.0</td>
      <td>1023.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2015-01-01 01:00:00</td>
      <td>Jan</td>
      <td>NaN</td>
      <td>4</td>
      <td>Y</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>30.0</td>
      <td>7.0</td>
      <td>1023.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2015-01-01 02:00:00</td>
      <td>Jan</td>
      <td>Bronx</td>
      <td>120</td>
      <td>Y</td>
      <td>3.0</td>
      <td>10.0</td>
      <td>30.0</td>
      <td>6.0</td>
      <td>1023.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2015-01-01 02:00:00</td>
      <td>Jan</td>
      <td>Brooklyn</td>
      <td>1229</td>
      <td>Y</td>
      <td>3.0</td>
      <td>10.0</td>
      <td>30.0</td>
      <td>6.0</td>
      <td>1023.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2015-01-01 02:00:00</td>
      <td>Jan</td>
      <td>EWR</td>
      <td>0</td>
      <td>Y</td>
      <td>3.0</td>
      <td>10.0</td>
      <td>30.0</td>
      <td>6.0</td>
      <td>1023.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
taxi.borough.value_counts()
```




    Bronx            4343
    Brooklyn         4343
    EWR              4343
    Manhattan        4343
    Queens           4343
    Staten Island    4343
    Name: borough, dtype: int64




```python
taxi.pickups.sum()
```




    14265773




```python
taxi.groupby('borough')\
        .agg({'pickups': 'sum'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pickups</th>
    </tr>
    <tr>
      <th>borough</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bronx</th>
      <td>220047</td>
    </tr>
    <tr>
      <th>Brooklyn</th>
      <td>2321035</td>
    </tr>
    <tr>
      <th>EWR</th>
      <td>105</td>
    </tr>
    <tr>
      <th>Manhattan</th>
      <td>10367841</td>
    </tr>
    <tr>
      <th>Queens</th>
      <td>1343528</td>
    </tr>
    <tr>
      <th>Staten Island</th>
      <td>6957</td>
    </tr>
  </tbody>
</table>
</div>




```python
taxi.groupby('borough').pickups.sum()
```




    borough
    Bronx              220047
    Brooklyn          2321035
    EWR                   105
    Manhattan        10367841
    Queens            1343528
    Staten Island        6957
    Name: pickups, dtype: int64




```python
min_pickups = taxi.groupby('borough').pickups.sum().idxmin()
```




    'EWR'




```python
taxi.groupby(['borough', 'hday'])\
        .agg({'pickups': 'mean'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>pickups</th>
    </tr>
    <tr>
      <th>borough</th>
      <th>hday</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Bronx</th>
      <th>N</th>
      <td>50.771073</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>48.065868</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Brooklyn</th>
      <th>N</th>
      <td>534.727969</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>527.011976</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">EWR</th>
      <th>N</th>
      <td>0.023467</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>0.041916</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Manhattan</th>
      <th>N</th>
      <td>2401.302921</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>2035.928144</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Queens</th>
      <th>N</th>
      <td>308.899904</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>320.730539</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Staten Island</th>
      <th>N</th>
      <td>1.606082</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>1.497006</td>
    </tr>
  </tbody>
</table>
</div>




```python
taxi.groupby(['borough', 'hday']).pickups.mean().to_frame()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>pickups</th>
    </tr>
    <tr>
      <th>borough</th>
      <th>hday</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Bronx</th>
      <th>N</th>
      <td>50.771073</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>48.065868</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Brooklyn</th>
      <th>N</th>
      <td>534.727969</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>527.011976</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">EWR</th>
      <th>N</th>
      <td>0.023467</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>0.041916</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Manhattan</th>
      <th>N</th>
      <td>2401.302921</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>2035.928144</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Queens</th>
      <th>N</th>
      <td>308.899904</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>320.730539</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Staten Island</th>
      <th>N</th>
      <td>1.606082</td>
    </tr>
    <tr>
      <th>Y</th>
      <td>1.497006</td>
    </tr>
  </tbody>
</table>
</div>




```python
pickups_by_mon_bor = taxi.groupby(['pickup_month', 'borough'], as_index=False)\
                                    .agg({'pickups': 'sum'})\
                                    .sort_values('pickups', ascending=False)
```


```python
print(pickups_by_mon_bor)
```

       pickup_month        borough  pickups
    21          Jun      Manhattan  1995388
    33          May      Manhattan  1888800
    9           Feb      Manhattan  1718571
    27          Mar      Manhattan  1661261
    3           Apr      Manhattan  1648278
    15          Jan      Manhattan  1455543
    19          Jun       Brooklyn   482466
    31          May       Brooklyn   476087
    1           Apr       Brooklyn   378095
    25          Mar       Brooklyn   346726
    7           Feb       Brooklyn   328650
    13          Jan       Brooklyn   309011
    22          Jun         Queens   286311
    34          May         Queens   275893
    28          Mar         Queens   219561
    4           Apr         Queens   216857
    10          Feb         Queens   185695
    16          Jan         Queens   159211
    30          May          Bronx    53037
    18          Jun          Bronx    49006
    0           Apr          Bronx    34617
    24          Mar          Bronx    32232
    6           Feb          Bronx    28694
    12          Jan          Bronx    22461
    23          Jun  Staten Island     1673
    35          May  Staten Island     1517
    5           Apr  Staten Island     1068
    29          Mar  Staten Island      975
    11          Feb  Staten Island      903
    17          Jan  Staten Island      821
    20          Jun            EWR       29
    32          May            EWR       27
    26          Mar            EWR       14
    8           Feb            EWR       14
    14          Jan            EWR       11
    2           Apr            EWR       10
    


```python
pickups_by_mon_bor.shape
```




    (36, 3)




```python
taxi.temp
```




    0        30.0
    1        30.0
    2        30.0
    3        30.0
    4        30.0
             ... 
    29096    75.0
    29097    75.0
    29098    75.0
    29099    75.0
    29100    75.0
    Name: temp, Length: 29101, dtype: float64




```python
def temp_to_celcius(series):
    return (series - 32) * 5 / 9
```


```python
temp_to_celcius(taxi.temp)
```




    0        -1.111111
    1        -1.111111
    2        -1.111111
    3        -1.111111
    4        -1.111111
               ...    
    29096    23.888889
    29097    23.888889
    29098    23.888889
    29099    23.888889
    29100    23.888889
    Name: temp, Length: 29101, dtype: float64




```python

```
