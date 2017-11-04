import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#plt.style.use('display.mpl_style', 'default') # Make the graphs a bit prettier
#figsize(15, 5)
#
#bad way to read csv data
# broken_df = pd.read_csv('/home/mohamed/Documents/Tps/Data_Analysis/temperat.csv')
# print broken_df[:3]
fixed_df = pd.read_csv('/home/mohamed/Documents/Tps/Data_Analysis/temperat.csv', sep=';', decimal='.', header=None ,encoding='latin1')
iris = fixed_df.values[[1,2,3],[1, 2,3]]
mat = fixed_df.as_matrix()

# print mat[[1:36]]
# print (iris)
# fixed_df['Janvier'].plot()
# panel = pd.Panel({'one' : fixed_df, 'two' : fixed_df - fixed_df.mean()})