import pandas as pd
import numpy as np


### Create a dummy pandas dataframe with a datetime index

df = pd.DataFrame(np.random.randn(1000, 3), columns=['a','b','c'], index=pd.date_range('20150101', periods=1000))


# then select only rows from years 2016 and 2017
df[df.index.year.isin([2016,2017])]


