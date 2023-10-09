import pandas as pd
import numpy as np
import os
data = pd.read_csv('D:\programs\pytest\ece228\project/test/seg_00be11.csv', dtype={'acoustic_data': np.int16, 'time_to_failure': np.float64}, nrows=150000)
print(data.shape)