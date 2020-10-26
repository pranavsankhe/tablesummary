import os
import numpy as np
import pandas as pd
from collections import defaultdict

'''
column name:
type:
cat_dictionary:
'''

class summary:
    def __init__(self, table, nan='nan', cat_thres=15):
        self.table = table
        self.column_name = self.table.columns
        self.nan = nan
        self.cat_thres = cat_thres

    def is_numerical(self, column_name):
        not_nan = 0
        num_count = 0
        for cell in self.table[column_name]:
            if cell != self.nan:
                not_nan += 1
            if cell.isnumeric():
                num_count += 1
        if num_count == not_nan:
            return True
        return False

    def is_categorical(self, column_name):
        cat = len(np.unique(self.table[column_name]))
        if cat < self.cat_thres:
            return True
        return False

    def column_stats(self, column_name):
        if self.is_categorical(column_name):
            categories, counts = np.unique(
                self.table[column_name], return_counts=True)
            total = counts.sum()
            for a, b in zip(categories, counts):
                print('\t{}: {:.2f}%'.format(a, (b/total)*100))
        else:
            print('Not Categorical')

    def summary(self):
        for column_name in self.column_name:
            print('--{}'.format(column_name))
            # if self.is_numerical(column_name):
            self.column_stats(column_name)