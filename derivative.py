from pyspark.sql import SparkSession
from pyspark.sql import SparkSession
from pyspark.sql.functions import lag, col
from pyspark.sql.window import Window
import matplotlib.pyplot as plt
import pandas as pd

def drop_values(df, column, values):
    return df.filter(~df[column].isin(values))

def derivative(df, column, interval):
    window_spec = Window.orderBy('Depth')
    derivative_col = f'derivative_{column}'
    df = df.withColumn(derivative_col, (col(column) - lag(col(column), interval).over(window_spec)) / interval)
    return df
