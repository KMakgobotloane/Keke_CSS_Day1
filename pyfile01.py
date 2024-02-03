# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 14:26:26 2024

@author: Keketso
"""

print("My First Python File")
# This is my first comment

# Valid names
x = 50
age = 50
_age= 50
my_age = 50
mYagE = 50
my_age_2 = 50

# Invalid names
# 2age = 50
# my age = 50
# my-age = 50

# Reading in files with Pandas
import pandas
file = pandas.read_csv("country_data.csv")
print(file)
"""
 Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""
print(file.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Age      11 non-null     int64 
 1   Gender   11 non-null     object
 2   Country  11 non-null     object
dtypes: int64(1), object(2)
"""
print(file.describe())
"""
 Age
count  11.000000
mean   33.363636
std     9.233339
min    22.000000
25%    27.000000
50%    30.000000
75%    39.500000
max    49.000000
"""
file = pandas.read_csv("iris.csv")
print(file)
"""
     sepal_length  sepal_width  petal_length  petal_width         species
0             5.1          3.5           1.4          0.2     Iris-setosa
1             4.9          3.0           1.4          0.2     Iris-setosa
2             4.7          3.2           1.3          0.2     Iris-setosa
3             4.6          3.1           1.5          0.2     Iris-setosa
4             5.0          3.6           1.4          0.2     Iris-setosa
..            ...          ...           ...          ...             ...
145           6.7          3.0           5.2          2.3  Iris-virginica
146           6.3          2.5           5.0          1.9  Iris-virginica
147           6.5          3.0           5.2          2.0  Iris-virginica
148           6.2          3.4           5.4          2.3  Iris-virginica
149           5.9          3.0           5.1          1.8  Iris-virginica

[150 rows x 5 columns]
"""
print(file.info())
"""<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   sepal_length  150 non-null    float64
 1   sepal_width   150 non-null    float64
 2   petal_length  150 non-null    float64
 3   petal_width   150 non-null    float64
 4   species       150 non-null    object 
dtypes: float64(4), object(1)
"""
print(file.describe())
"""
       sepal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000
"""

file = pandas.read_csv("diab_data.csv")
print(file)
"""
     preg_count  glucose  bp  skinfold  insulin   BMI  predigree  age  class
0             6      148  72        35        0  33.6      0.627   50      1
1             1       85  66        29        0  26.6      0.351   31      0
2             8      183  64         0        0  23.3      0.672   32      1
3             1       89  66        23       94  28.1      0.167   21      0
4             0      137  40        35      168  43.1      2.288   33      1
..          ...      ...  ..       ...      ...   ...        ...  ...    ...
763          10      101  76        48      180  32.9      0.171   63      0
764           2      122  70        27        0  36.8      0.340   27      0
765           5      121  72        23      112  26.2      0.245   30      0
766           1      126  60         0        0  30.1      0.349   47      1
767           1       93  70        31        0  30.4      0.315   23      0

[768 rows x 9 columns]
"""
print(file.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 768 entries, 0 to 767
Data columns (total 9 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   preg_count  768 non-null    int64  
 1   glucose     768 non-null    int64  
 2   bp          768 non-null    int64  
 3   skinfold    768 non-null    int64  
 4   insulin     768 non-null    int64  
 5   BMI         768 non-null    float64
 6   predigree   768 non-null    float64
 7   age         768 non-null    int64  
 8   class       768 non-null    int64  
dtypes: float64(2), int64(7)
"""
print(file.describe())
"""
       preg_count     glucose          bp  ...   predigree         age       class
count  768.000000  768.000000  768.000000  ...  768.000000  768.000000  768.000000
mean     3.845052  120.894531   69.105469  ...    0.471876   33.240885    0.348958
std      3.369578   31.972618   19.355807  ...    0.331329   11.760232    0.476951
min      0.000000    0.000000    0.000000  ...    0.078000   21.000000    0.000000
25%      1.000000   99.000000   62.000000  ...    0.243750   24.000000    0.000000
50%      3.000000  117.000000   72.000000  ...    0.372500   29.000000    0.000000
75%      6.000000  140.250000   80.000000  ...    0.626250   41.000000    1.000000
max     17.000000  199.000000  122.000000  ...    2.420000   81.000000    1.000000

[8 rows x 9 columns]
"""
file = pandas.read_csv("housing_data.csv")
print(file)
"""
 0.00632   18   2.31    0  0.538  6.575  ...  1    296  15.3   396.9  4.98    24
0    0.02731  0.0   7.07  0.0  0.469  6.421  ...  2  242.0  17.8  396.90  9.14  21.6
1    0.02729  0.0   7.07  0.0  0.469  7.185  ...  2  242.0  17.8  392.83  4.03  34.7
2    0.03237  0.0   2.18  0.0  0.458  6.998  ...  3  222.0  18.7  394.63  2.94  33.4
3    0.06905  0.0   2.18  0.0  0.458  7.147  ...  3  222.0  18.7  396.90  5.33  36.2
4    0.02985  0.0   2.18  0.0  0.458  6.430  ...  3  222.0  18.7  394.12  5.21  28.7
..       ...  ...    ...  ...    ...    ...  ... ..    ...   ...     ...   ...   ...
500  0.06263  0.0  11.93  0.0  0.573  6.593  ...  1  273.0  21.0  391.99  9.67  22.4
501  0.04527  0.0  11.93  0.0  0.573  6.120  ...  1  273.0  21.0  396.90  9.08  20.6
502  0.06076  0.0  11.93  0.0  0.573  6.976  ...  1  273.0  21.0  396.90  5.64  23.9
503  0.10959  0.0  11.93  0.0  0.573  6.794  ...  1  273.0  21.0  393.45  6.48  22.0
504  0.04741  0.0  11.93  0.0  0.573  6.030  ...  1  273.0  21.0  396.90  7.88  11.9

[505 rows x 14 columns]
"""
print(file.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 505 entries, 0 to 504
Data columns (total 14 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   0.00632  505 non-null    float64
 1   18       505 non-null    float64
 2   2.31     505 non-null    float64
 3   0        505 non-null    float64
 4   0.538    505 non-null    float64
 5   6.575    505 non-null    float64
 6   65.2     505 non-null    float64
 7   4.09     505 non-null    float64
 8   1        505 non-null    int64  
 9   296      505 non-null    float64
 10  15.3     505 non-null    float64
 11  396.9    505 non-null    float64
 12  4.98     505 non-null    float64
 13  24       451 non-null    float64
dtypes: float64(13), int64(1)
"""
print(file.describe())
"""
         0.00632          18        2.31  ...       396.9        4.98          24
count  505.000000  505.000000  505.000000  ...  505.000000  505.000000  451.000000
mean     1.271696   13.285941    9.218812  ...  332.664158   11.550792   23.749889
std      2.400926   23.070598    7.170151  ...  125.414151    6.063900    8.818376
min      0.000000    0.000000    0.000000  ...    0.320000    1.730000    6.300000
25%      0.049810    0.000000    3.440000  ...  364.610000    6.900000   18.500000
50%      0.144760    0.000000    6.960000  ...  390.640000   10.400000   21.900000
75%      0.825260   18.100000   18.100000  ...  395.600000   15.020000   26.600000
max      9.966540  100.000000   27.740000  ...  396.900000   34.410000   50.000000

[8 rows x 14 columns]
"""

# file = pandas.read_txt(insurance_data.txt)
# print(file)
"""
AttributeError: module 'pandas' has no attribute 'read_txt'
"""
# file = pandas.read_csv("insurance_data.csv")
# print(file)
"""
ParserError: Error tokenizing data. C error: Expected 1 fields in line 7, saw 2
"""
file = pandas.read_csv("UpperVaalWaterStrike_wbw_202285_124651_DataExport_1 (2).csv")
print(file)
"""
 GeositeInfo_DataOwner  ... WaterStrike_ContributionValue
0      Dept Water - Pretoria  ...                           NaN
1      Dept Water - Pretoria  ...                           NaN
2      Dept Water - Pretoria  ...                           NaN
3      Dept Water - Pretoria  ...                           NaN
4      Dept Water - Pretoria  ...                           NaN
                     ...  ...                           ...
17789  Dept Water - Pretoria  ...                           NaN
17790  Dept Water - Pretoria  ...                           NaN
17791  Dept Water - Pretoria  ...                           NaN
17792  Dept Water - Pretoria  ...                           NaN
17793  Dept Water - Pretoria  ...                           NaN

[17794 rows x 13 columns]
"""
print(file.info())
"""
 #   Column                                  Non-Null Count  Dtype  
---  ------                                  --------------  -----  
 0   GeositeInfo_DataOwner                   17794 non-null  object 
 1   GeositeInfo_Identifier                  17794 non-null  object 
 2   GeositeInfo_GeositeType                 17794 non-null  object 
 3   GeositeInfo_Latitude                    17794 non-null  float64
 4   GeositeInfo_Longitude                   17794 non-null  float64
 5   WaterStrike_ConstructionCompletionDate  11612 non-null  object 
 6   WaterStrike_YieldMeasurementMethod      926 non-null    object 
 7   WaterStrike_WaterStrikeType             11738 non-null  object 
 8   WaterStrike_SeepageValue                5287 non-null   float64
 9   WaterStrike_DepthToTop                  11737 non-null  float64
 10  WaterStrike_DepthToBottom               236 non-null    float64
 11  WaterStrike_TotalBlowYieldValue         8022 non-null   float64
 12  WaterStrike_ContributionValue           1414 non-null   float64
dtypes: float64(7), object(6)
"""
print(file.describe())
"""
       GeositeInfo_Latitude  ...  WaterStrike_ContributionValue
count          17794.000000  ...                    1414.000000
mean             -26.851910  ...                       2.840170
std                0.588503  ...                       9.313266
min              -28.758110  ...                       0.100000
25%              -27.008878  ...                       0.400000
50%              -26.675435  ...                       0.900000
75%              -26.429787  ...                       2.000000
max              -25.905660  ...                     121.100000

[8 rows x 7 columns]
"""

# 4. Storing Data in Python
B1 = 30
B2 = 40
B3 = 30
B4 = 49
print(B1)
"""
30
"""
print(B2)
"""
40
"""

# Using lists
age = [30,40,30,49,22,35,22,46,29,25,39]
print(age)
"""
[30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39]
"""
#Lists indexes start at 0 which has the value of 30
print(age[0])
"""
30
"""
print(age[1])
"""
40
"""
print(age[10])
"""
39
"""
# print(age[11])
"""
IndexError: list index out of range
"""
age = [30,40,30,49,22,35,22,46,29,25,39]
print(min(age))
"""
22
"""
print(max(age))
"""
49
"""
print(len(age))
"""
49
"""
print(sum(age))
"""
11
"""
average = sum(age)/len(age)
"""
367
"""
print(average)
"""
33.36363636363637
"""

# Storing text
# C2 = M
# C3 = M
# C4 = F
"""
NameError: name 'M' is not defined
"""
C2 = "M"
C3 = "M"
C4 = "F"
print(C2)
"""
M
"""
print(C3)
"""
M
"""
print(C4)
"""
F
"""
gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])
"""
M
M
F
M
"""
country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]
print(country)
print(country[0])
print(country[5])
"""
['South Africa', 'Botswana', 'South Africa', 'South Africa', 'Kenya', 'Mozambique', 'Lesotho', 'Kenya', 'Kenya', 'Egypt', 'Sudan']
South Africa
Mozambique
"""
# Data Storage With Lists
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list)
"""
[42, -2021, 6.283, 'tau', 'node']
"""
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list) 
print(my_list[:])
"""
[42, -2021, 6.283, 'tau', 'node']
[42, -2021, 6.283, 'tau', 'node']
"""
my_list.append("pi")
print(my_list)
"""
[42, -2021, 6.283, 'tau', 'node', 'pi']
"""
my_list.insert(1,"pi2")
print(my_list)
"""
[42, 'pi2', -2021, 6.283, 'tau', 'node', 'pi']
"""
my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))
"""
[42, -2021, 6.283, 'node']
4
"""
print(my_list[0:3])
"""
[42, -2021, 6.283]
"""
# Dictionaries
# The syntax for creating a dictionary is as follows:

# d = {'key1': 'value1', 'key2': 'value2'}

person = {'name': 'John Doe', 'age': 30, 'address': '123 Main St.'}
print(person['name']) # 'John Doe'
print(person.get('age')) # 30
person['phone'] = '555-555-5555'
print(person['phone'])
"""
John Doe
30
555-555-5555
"""
import pandas as pd

# Creating a DataFrame
data = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}

#df = data frame
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)
"""
 age gender       country
0    30      M  South Africa
1    40      M      Botswana
2    30      F  South Africa
3    49      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    46      M         Kenya
8    29      M         Kenya
9    25      F         Egypt
10   39      M         Sudan
"""
# Accessing specific columns
print(df['age'])
print(df['gender'])
"""
Name: gender, dtype: object
"""
# Basic statistics
print(df['age'].min())
print(df['age'].max())
print(df['age'].mean())
"""
22
49
33.36363636363637
"""
# Filtering data
print(df[df['age'] > 30])
"""
  age gender       country
1    40      M      Botswana
3    49      M  South Africa
5    35      F    Mozambique
7    46      M         Kenya
10   39      M         Sudan
"""
# Slicing rows and columns
print(df[1:4])  # Select rows 1 to 3 and all columns
"""
  age gender       country
1   40      M      Botswana
2   30      F  South Africa
3   49      M  South Africa
"""
# Adding a new column
df['new_column'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(df)
"""
 age gender       country  new_column
0    30      M  South Africa           1
1    40      M      Botswana           2
2    30      F  South Africa           3
3    49      M  South Africa           4
4    22      F         Kenya           5
5    35      F    Mozambique           6
6    22      F       Lesotho           7
7    46      M         Kenya           8
8    29      M         Kenya           9
9    25      F         Egypt          10
10   39      M         Sudan          11
"""
# Removing a column
df.drop(columns=['new_column'], inplace=True)
print(df)
"""
age gender       country
0    30      M  South Africa
1    40      M      Botswana
2    30      F  South Africa
3    49      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    46      M         Kenya
8    29      M         Kenya
9    25      F         Egypt
10   39      M         Sudan
"""
