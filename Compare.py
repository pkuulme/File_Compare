import pandas as pd
second = 'teine.xlsx'
first = 'esimene.xlsx'



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
merged[merged['_merge'] == 'right_only']

writer = pd.ExcelWriter('output.xlsx')
merged.to_excel(writer,'Sheet1')
writer.save()

