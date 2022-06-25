```python
#Импортируем библиотеку, файл с данными записываем в bookings
import pandas as pd
bookings = pd.read_csv('C:/Users/мой компьютер/Downloads/2_bookings.csv', sep = ';')
```


```python
#Изучаем имеющиеся данные: формат, размер, содержимое
bookings.head(10)
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
      <th>Hotel</th>
      <th>Is Canceled</th>
      <th>Lead Time</th>
      <th>arrival full date</th>
      <th>Arrival Date Year</th>
      <th>Arrival Date Month</th>
      <th>Arrival Date Week Number</th>
      <th>Arrival Date Day of Month</th>
      <th>Stays in Weekend nights</th>
      <th>Stays in week nights</th>
      <th>...</th>
      <th>Adults</th>
      <th>Children</th>
      <th>Babies</th>
      <th>Meal</th>
      <th>Country</th>
      <th>Reserved Room Type</th>
      <th>Assigned room type</th>
      <th>customer type</th>
      <th>Reservation Status</th>
      <th>Reservation status_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Resort Hotel</td>
      <td>0</td>
      <td>342</td>
      <td>2015-07-01</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>2</td>
      <td>0.0</td>
      <td>0</td>
      <td>BB</td>
      <td>PRT</td>
      <td>C</td>
      <td>C</td>
      <td>Transient</td>
      <td>Check-Out</td>
      <td>2015-07-01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Resort Hotel</td>
      <td>0</td>
      <td>737</td>
      <td>2015-07-01</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>2</td>
      <td>0.0</td>
      <td>0</td>
      <td>BB</td>
      <td>PRT</td>
      <td>C</td>
      <td>C</td>
      <td>Transient</td>
      <td>Check-Out</td>
      <td>2015-07-01</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Resort Hotel</td>
      <td>0</td>
      <td>7</td>
      <td>2015-07-01</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>0.0</td>
      <td>0</td>
      <td>BB</td>
      <td>GBR</td>
      <td>A</td>
      <td>C</td>
      <td>Transient</td>
      <td>Check-Out</td>
      <td>2015-07-02</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Resort Hotel</td>
      <td>0</td>
      <td>13</td>
      <td>2015-07-01</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>0.0</td>
      <td>0</td>
      <td>BB</td>
      <td>GBR</td>
      <td>A</td>
      <td>A</td>
      <td>Transient</td>
      <td>Check-Out</td>
      <td>2015-07-02</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Resort Hotel</td>
      <td>0</td>
      <td>14</td>
      <td>2015-07-01</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>2</td>
      <td>0.0</td>
      <td>0</td>
      <td>BB</td>
      <td>GBR</td>
      <td>A</td>
      <td>A</td>
      <td>Transient</td>
      <td>Check-Out</td>
      <td>2015-07-03</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Resort Hotel</td>
      <td>0</td>
      <td>14</td>
      <td>2015-07-01</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>2</td>
      <td>0.0</td>
      <td>0</td>
      <td>BB</td>
      <td>GBR</td>
      <td>A</td>
      <td>A</td>
      <td>Transient</td>
      <td>Check-Out</td>
      <td>2015-07-03</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Resort Hotel</td>
      <td>0</td>
      <td>0</td>
      <td>2015-07-01</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>2</td>
      <td>0.0</td>
      <td>0</td>
      <td>BB</td>
      <td>PRT</td>
      <td>C</td>
      <td>C</td>
      <td>Transient</td>
      <td>Check-Out</td>
      <td>2015-07-03</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Resort Hotel</td>
      <td>0</td>
      <td>9</td>
      <td>2015-07-01</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>2</td>
      <td>0.0</td>
      <td>0</td>
      <td>FB</td>
      <td>PRT</td>
      <td>C</td>
      <td>C</td>
      <td>Transient</td>
      <td>Check-Out</td>
      <td>2015-07-03</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Resort Hotel</td>
      <td>1</td>
      <td>85</td>
      <td>2015-07-01</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>...</td>
      <td>2</td>
      <td>0.0</td>
      <td>0</td>
      <td>BB</td>
      <td>PRT</td>
      <td>A</td>
      <td>A</td>
      <td>Transient</td>
      <td>Canceled</td>
      <td>2015-05-06</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Resort Hotel</td>
      <td>1</td>
      <td>75</td>
      <td>2015-07-01</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>...</td>
      <td>2</td>
      <td>0.0</td>
      <td>0</td>
      <td>HB</td>
      <td>PRT</td>
      <td>D</td>
      <td>D</td>
      <td>Transient</td>
      <td>Canceled</td>
      <td>2015-04-22</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 21 columns</p>
</div>




```python
bookings.shape #количество строк и колонок в датафрейме
```




    (119390, 21)




```python
bookings.dtypes #тип данных
```




    Hotel                         object
    Is Canceled                    int64
    Lead Time                      int64
    arrival full date             object
    Arrival Date Year              int64
    Arrival Date Month            object
    Arrival Date Week Number       int64
    Arrival Date Day of Month      int64
    Stays in Weekend nights        int64
    Stays in week nights           int64
    stays total nights             int64
    Adults                         int64
    Children                     float64
    Babies                         int64
    Meal                          object
    Country                       object
    Reserved Room Type            object
    Assigned room type            object
    customer type                 object
    Reservation Status            object
    Reservation status_date       object
    dtype: object




```python
#Приводим наименования колонок к удобному для работы виду, переводим все заглавные в сточные, заменяем пробелы на "_"

bookings = bookings.rename(columns=lambda c: c.lower().replace(' ', '_'))  
```


```python
#Выясним из каких стран наибольшее число успешных бронирований. Бронирование считается успешным, если в дальнейшем не было отменено (переменная is_canceled)

bookings.groupby('country', as_index=False).is_canceled.value_counts().sort_values('count', ascending=False).head(10)
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
      <th>country</th>
      <th>is_canceled</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>222</th>
      <td>PRT</td>
      <td>1</td>
      <td>27519</td>
    </tr>
    <tr>
      <th>223</th>
      <td>PRT</td>
      <td>0</td>
      <td>21071</td>
    </tr>
    <tr>
      <th>98</th>
      <td>GBR</td>
      <td>0</td>
      <td>9676</td>
    </tr>
    <tr>
      <th>92</th>
      <td>FRA</td>
      <td>0</td>
      <td>8481</td>
    </tr>
    <tr>
      <th>83</th>
      <td>ESP</td>
      <td>0</td>
      <td>6391</td>
    </tr>
    <tr>
      <th>69</th>
      <td>DEU</td>
      <td>0</td>
      <td>6069</td>
    </tr>
    <tr>
      <th>126</th>
      <td>IRL</td>
      <td>0</td>
      <td>2543</td>
    </tr>
    <tr>
      <th>99</th>
      <td>GBR</td>
      <td>1</td>
      <td>2453</td>
    </tr>
    <tr>
      <th>135</th>
      <td>ITA</td>
      <td>0</td>
      <td>2433</td>
    </tr>
    <tr>
      <th>84</th>
      <td>ESP</td>
      <td>1</td>
      <td>2177</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Вычисляем на сколько в среднем ночей бронируют отели 
bookings.groupby('hotel', as_index=False).stays_total_nights.mean().round(2)
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
      <th>hotel</th>
      <th>stays_total_nights</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>City Hotel</td>
      <td>2.98</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Resort Hotel</td>
      <td>4.32</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Вычисляем количество бронирований, в которых тип номера, присвоенный клиенту, отличается от изначально забронированного
bookings.query('assigned_room_type != reserved_room_type')
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
      <th>hotel</th>
      <th>is_canceled</th>
      <th>lead_time</th>
      <th>arrival_full_date</th>
      <th>arrival_date_year</th>
      <th>arrival_date_month</th>
      <th>arrival_date_week_number</th>
      <th>arrival_date_day_of_month</th>
      <th>stays_in_weekend_nights</th>
      <th>stays_in_week_nights</th>
      <th>...</th>
      <th>adults</th>
      <th>children</th>
      <th>babies</th>
      <th>meal</th>
      <th>country</th>
      <th>reserved_room_type</th>
      <th>assigned_room_type</th>
      <th>customer_type</th>
      <th>reservation_status</th>
      <th>reservation_status_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>Resort Hotel</td>
      <td>0</td>
      <td>7</td>
      <td>2015-07-01</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>0.0</td>
      <td>0</td>
      <td>BB</td>
      <td>GBR</td>
      <td>A</td>
      <td>C</td>
      <td>Transient</td>
      <td>Check-Out</td>
      <td>2015-07-02</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Resort Hotel</td>
      <td>0</td>
      <td>68</td>
      <td>2015-07-01</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>2</td>
      <td>0.0</td>
      <td>0</td>
      <td>BB</td>
      <td>USA</td>
      <td>D</td>
      <td>E</td>
      <td>Transient</td>
      <td>Check-Out</td>
      <td>2015-07-05</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Resort Hotel</td>
      <td>0</td>
      <td>68</td>
      <td>2015-07-01</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>2</td>
      <td>0.0</td>
      <td>0</td>
      <td>BB</td>
      <td>IRL</td>
      <td>D</td>
      <td>E</td>
      <td>Transient</td>
      <td>Check-Out</td>
      <td>2015-07-05</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Resort Hotel</td>
      <td>0</td>
      <td>12</td>
      <td>2015-07-01</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>2</td>
      <td>0.0</td>
      <td>0</td>
      <td>BB</td>
      <td>IRL</td>
      <td>A</td>
      <td>E</td>
      <td>Transient</td>
      <td>Check-Out</td>
      <td>2015-07-02</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Resort Hotel</td>
      <td>0</td>
      <td>0</td>
      <td>2015-07-01</td>
      <td>2015</td>
      <td>July</td>
      <td>27</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>2</td>
      <td>0.0</td>
      <td>0</td>
      <td>BB</td>
      <td>FRA</td>
      <td>A</td>
      <td>G</td>
      <td>Transient</td>
      <td>Check-Out</td>
      <td>2015-07-02</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>119273</th>
      <td>City Hotel</td>
      <td>0</td>
      <td>213</td>
      <td>2017-08-28</td>
      <td>2017</td>
      <td>August</td>
      <td>35</td>
      <td>28</td>
      <td>1</td>
      <td>3</td>
      <td>...</td>
      <td>1</td>
      <td>0.0</td>
      <td>0</td>
      <td>HB</td>
      <td>PRT</td>
      <td>A</td>
      <td>K</td>
      <td>Transient-Party</td>
      <td>Check-Out</td>
      <td>2017-09-01</td>
    </tr>
    <tr>
      <th>119274</th>
      <td>City Hotel</td>
      <td>0</td>
      <td>213</td>
      <td>2017-08-28</td>
      <td>2017</td>
      <td>August</td>
      <td>35</td>
      <td>28</td>
      <td>1</td>
      <td>3</td>
      <td>...</td>
      <td>1</td>
      <td>0.0</td>
      <td>0</td>
      <td>HB</td>
      <td>PRT</td>
      <td>A</td>
      <td>K</td>
      <td>Transient-Party</td>
      <td>Check-Out</td>
      <td>2017-09-01</td>
    </tr>
    <tr>
      <th>119289</th>
      <td>City Hotel</td>
      <td>0</td>
      <td>25</td>
      <td>2017-08-30</td>
      <td>2017</td>
      <td>August</td>
      <td>35</td>
      <td>30</td>
      <td>0</td>
      <td>3</td>
      <td>...</td>
      <td>3</td>
      <td>0.0</td>
      <td>0</td>
      <td>BB</td>
      <td>ITA</td>
      <td>E</td>
      <td>F</td>
      <td>Transient</td>
      <td>Check-Out</td>
      <td>2017-09-02</td>
    </tr>
    <tr>
      <th>119297</th>
      <td>City Hotel</td>
      <td>0</td>
      <td>332</td>
      <td>2017-08-31</td>
      <td>2017</td>
      <td>August</td>
      <td>35</td>
      <td>31</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>2</td>
      <td>0.0</td>
      <td>0</td>
      <td>BB</td>
      <td>GBR</td>
      <td>D</td>
      <td>F</td>
      <td>Transient</td>
      <td>Check-Out</td>
      <td>2017-09-02</td>
    </tr>
    <tr>
      <th>119357</th>
      <td>City Hotel</td>
      <td>0</td>
      <td>47</td>
      <td>2017-08-31</td>
      <td>2017</td>
      <td>August</td>
      <td>35</td>
      <td>31</td>
      <td>1</td>
      <td>3</td>
      <td>...</td>
      <td>1</td>
      <td>0.0</td>
      <td>0</td>
      <td>SC</td>
      <td>PRT</td>
      <td>A</td>
      <td>D</td>
      <td>Transient</td>
      <td>Check-Out</td>
      <td>2017-09-04</td>
    </tr>
  </tbody>
</table>
<p>14917 rows × 21 columns</p>
</div>




```python
#Высняем какие месяцы были самыми пользовались наибольшим спросом при бронировании на 2016 и 2017 год
bookings.groupby('arrival_date_year', as_index=False).arrival_date_month.value_counts().sort_values('count', ascending=False).head(10)
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
      <th>arrival_date_year</th>
      <th>arrival_date_month</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>18</th>
      <td>2017</td>
      <td>May</td>
      <td>6313</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016</td>
      <td>October</td>
      <td>6203</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2017</td>
      <td>April</td>
      <td>5661</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2017</td>
      <td>June</td>
      <td>5647</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2016</td>
      <td>May</td>
      <td>5478</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2016</td>
      <td>April</td>
      <td>5428</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016</td>
      <td>September</td>
      <td>5394</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2017</td>
      <td>July</td>
      <td>5313</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016</td>
      <td>June</td>
      <td>5292</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2015</td>
      <td>September</td>
      <td>5114</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Выясняем в какие месяцы было больше всего отмен бронирования в 2015, 2016, 2017 гг.
bookings.query('is_canceled == 1').groupby('arrival_date_year', as_index=False).arrival_date_month.value_counts().sort_values('count', ascending=False).head(10)
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
      <th>arrival_date_year</th>
      <th>arrival_date_month</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>18</th>
      <td>2017</td>
      <td>May</td>
      <td>2762</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016</td>
      <td>October</td>
      <td>2514</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2017</td>
      <td>April</td>
      <td>2463</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2017</td>
      <td>June</td>
      <td>2439</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2016</td>
      <td>June</td>
      <td>2096</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2015</td>
      <td>September</td>
      <td>2094</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2016</td>
      <td>April</td>
      <td>2061</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016</td>
      <td>September</td>
      <td>2022</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2017</td>
      <td>July</td>
      <td>1984</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016</td>
      <td>May</td>
      <td>1915</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Оределили наибольшее среднее значение числовых колонок 'adults', 'children', 'babies'
bookings[['adults', 'children', 'babies']].mean()
```




    adults      1.856403
    children    0.103890
    babies      0.007949
    dtype: float64




```python
#Посчитали общее количество детей для каждой записи, создали новую колонку с полученными данными 
bookings['total_kids'] = bookings['children'] + bookings['babies']
```


```python
#Выяснили в отелях какого типа чаще оформляют бронирования семьи с детьми
bookings.groupby('hotel', as_index=False).total_kids.mean().round(2)
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
      <th>hotel</th>
      <th>total_kids</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>City Hotel</td>
      <td>0.10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Resort Hotel</td>
      <td>0.14</td>
    </tr>
  </tbody>
</table>
</div>



Не все бронирования завершились успешно (`is_canceled`), поэтому можно посчитать, сколько клиентов было потеряно в процессе. Иными словами, посчитать метрику под названием **Churn Rate**.

**Churn rate** (отток, коэффициент оттока) – это процент подписчиков (например, на push-уведомления от сайта), которые отписались от канала коммуникации, отказались от услуг сервиса в течение определенного периода времени. Иными словами, представляет собой отношение количества ушедших пользователей к общему количеству пользователей, выраженное в процентах.

В нашем случае **Churn Rate** - это процент клиентов, которые отменили бронирование. Давайте посмотрим, как эта метрика связана с наличием детей у клиентов!

Создайте переменную `has_kids`, которая принимает значение `True`, если клиент при бронировании указал хотя бы одного ребенка (`total_kids`), в противном случае – `False`. Далее проверьте, среди какой группы пользователей показатель оттока выше. 


```python
#Вычислили количество клиентов, которые при бронировании указали наличие детей (1 вариант)
bookings['has_kids'] = bookings.total_kids.apply(lambda x: True if x > 0 else False)
bookings['has_kids'].value_counts()
```




    False    110058
    True       9332
    Name: has_kids, dtype: int64




```python
#Вычислили количество клиентов, которые при бронировании указали наличие детей (2 вариант)
bookings['has_kids'] = bookings.total_kids.astype(bool)
bookings['has_kids'].value_counts()
```




    False    110054
    True       9336
    Name: has_kids, dtype: int64




```python
#Посчитали количество состоявшихся и отмененных бронирований по катериям: с детьми, без детей
bookings[['has_kids', 'is_canceled']].value_counts()
```




    has_kids  is_canceled
    False     0              69093
              1              40961
    True      0               6073
              1               3263
    dtype: int64




```python
#Посчитали в какой категории, с детьми или без детей, процент отмененных бронирований выше
bookings[['has_kids', 'is_canceled']].value_counts() / bookings[['has_kids']].value_counts() * 100
```




    has_kids  is_canceled
    False     0              62.780998
              1              37.219002
    True      0              65.049272
              1              34.950728
    dtype: float64




```python

```
