# [Данные](https://github.com/KristinaLyu/Tasks_from_Karpov_courses/blob/main/taxi_NYC/2_taxi_nyc.csv) о поездках на такси в Нью-Йорке
### в которых также имеется информация о погодных условиях и выходных днях

*pickup_dt* – период с точностью до часа
*pickup_month* – месяц
*borough* – район Нью-Йорка, из которого был сделан заказ (5 районов + аэропорт)
*pickups* – число поездок за период (час)
*hday* – является ли день праздничным/выходным; Y - да,  N - нет
*spd* – скорость ветра в милях в час
*vsb* – видимость
*temp* – температура в градусах Фаренгейта
*dewp* – точка росы по Фаренгейту
*slp* – давление
*pcp_01* – количество осадков за час
*pcp_06* – количество осадков за 6 часов
*pcp_24* – количество осадков за 24 часа
*sd* – глубина снега в дюймах

```python
import pandas as pd
taxi = pd.read_csv('C:/Users/мой компьютер/Downloads/2_taxi_nyc.csv') 
```
Датасет сохранили в переменую **taxi**
```python
taxi.shape
```
Размер датасета **(29101 строка, 14 столбцов)**
```python
taxi.dtypes
```
Тип, преобладающий в датасете **float64**
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
В названиях столбцов **pcp 01, pcp 06, pcp 24** встречался пробел, внесли изменения для удобства дальнейшей работы и сохранили изменения в исходном датафрэйме.
```python
taxi.borough.value_counts()
```
Для того, чтобы узнать информацию о поездках из определенного района города, посмотрели количество записей(строк) по каждому району, откуда совершались поездки.
```python
taxi.pickups.sum()
```
Сначала узнали суммарное количество всех поездок, записанных в датасете, далее агрегировали сумму по каждому и районов так:
```python
taxi.groupby('borough')\
        .agg({'pickups': 'sum'})
```
или можно так:
```python
taxi.groupby('borough').pickups.sum()
```
Далее, выяснили район, из кторого совершалось минимальное количество поездок - **EWR**
```python
min_pickups = taxi.groupby('borough').pickups.sum().idxmin()
```
Также выяснили, в каких районах среднее колиество поездок в выходные больше, чем в будние дни:
```python
taxi.groupby(['borough', 'hday'])\
        .agg({'pickups': 'mean'})
```
еще можно вот так:
```python
taxi.groupby(['borough', 'hday']).pickups.mean().to_frame()
```
Отсортировали по убывания количества поездок по месяцам и районам: 
```python
taxi.groupby(['pickup_month', 'borough'], as_index=False)\
                                    .agg({'pickups': 'sum'})\
                                    .sort_values('pickups', ascending=False)
```
И в заключении, потренировались с переводом градусов из Фаренгейта в Цельсия, с применением функции:
```python
taxi.temp
```
```python
def temp_to_celcius(series):
    return (series - 32) * 5 / 9
temp_to_celcius(taxi.temp)
````
Весь код, с выводом результатов запросов можно посмотреть [тут](https://github.com/KristinaLyu/Tasks_from_Karpov_courses/blob/main/taxi_NYC/DF_taxi.ipynb)
