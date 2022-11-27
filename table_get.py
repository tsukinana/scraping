#!/usr/bin/env python
#-*-coding: utf-8-*-

import pandas as pd

url=""

data =pd.read_html(url,header=0)
print(data[0].head())
#データフレームをクリップボードにコピー可能
data[0].to_clipboard()