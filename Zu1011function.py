import pandas as pd
import timeit

#Functions
def mean_with_sum(row: pd.Series):
    return row.sum()/len(row)

def mean_pandas(row: pd.Series):
    return row.mean()

def correlation_with_sums(table: pd.DateOffset, col1: str, col2:str)->float:
    x= table[col1]
    y=table[col2]
    n = len(x)
    mean_x = x.mean()
    mean_y = y.mean()
    x_i_minus_mean_x = [x_i - mean_x for x_i in x]
    y_i_minus_mean_y = [y_i - mean_y for y_i in y]

    cov_without_den = sum([x_i_minus_mean_x[i]*y_i_minus_mean_y[i] for i in range(n)])

    std_dev_x = sum([el**2 for el in x_i_minus_mean_x])
    std_dev_y = sum([el**2 for el in y_i_minus_mean_y])

    return cov_without_den/((std_dev_x* std_dev_y)**0.5)

#Tests MEAN
def test_mean_pandas():
    SETUP_CODE='''
from __main__ import mean_pandas
from random import uniform
import pandas as pd'''

    TEST_CODE = '''
test_list = pd.Series([uniform(-1000,1000) for _ in range (1000)])
mean_pandas(test_list)'''

    time_pandas = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE, repeat = 5, number = 10000)
    print(time_pandas)

def test_mean_with_sum():
    SETUP_CODE='''
from __main__ import mean_with_sum
from random import uniform
import pandas as pd'''

    TEST_CODE = '''
test_list = pd.Series([uniform(-1000,1000) for _ in range (1000)])
mean_with_sum(test_list)'''

    time_pandas = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE, repeat = 5, number = 10000)
    print(time_pandas)

#Tests Correlation
def test_corr_sums():
    SETUP_CODE='''
from __main__ import correlation_with_sums
from random import uniform
import pandas as pd'''

    TEST_CODE = '''
test_list_x = pd.Series([uniform(-1000,1000) for _ in range (1000)])
test_list_y = pd.Series([uniform(-1000,1000) for _ in range (1000)])
df = pd.DataFrame(list(zip(test_list_x, test_list_y)),
               columns =['A', 'B'])
correlation_with_sums(df, "A", "B")'''

    time_pandas = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE, repeat=5, number = 10000)
    print(time_pandas)

def test_corr_pandas():
    SETUP_CODE='''
from charts import r_value
from random import uniform
import pandas as pd'''

    TEST_CODE = '''
test_list_x = pd.Series([uniform(-1000,1000) for _ in range (1000)])
test_list_y = pd.Series([uniform(-1000,1000) for _ in range (1000)])
df = pd.DataFrame(list(zip(test_list_x, test_list_y)),
               columns =['A', 'B'])
r_value(df, "A", "B")'''

    time_pandas = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE, repeat=5, number = 10000)
    print(time_pandas)

def compare_mean():
    test_mean_pandas()
    test_mean_with_sum()

def compare_corr():
    test_corr_pandas()
    test_corr_sums()

if __name__ == "__main__":
    compare_corr()
