import pandas as pd
from tkinter.filedialog import askopenfilename
import tkinter.filedialog as tk


first = tk.askopenfilename(title='Select first file')
second = askopenfilename(title='Select second file')

uno = pd.read_excel(first,
sheet_name=0,
header=0,
index_col=False,
keep_default_na=True
)

dos = pd.read_excel(second,
sheet_name=0,
header=0,
index_col=False,
keep_default_na=True
)

merged = uno.merge(dos, indicator=True,how='outer')

writer = pd.ExcelWriter('output.xlsx')
merged.to_excel(writer,'Sheet1')
writer.save()

