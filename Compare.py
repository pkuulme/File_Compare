import pandas as pd
import tkinter.filedialog as tk
from tkinter import messagebox


class Files():

    first = tk.askopenfilename(title='Select first file')
    second = tk.askopenfilename(title='Select second file')

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
class comparing():
    merged = Files.uno.merge(Files.dos, indicator=True,how='outer')

    writer = pd.ExcelWriter('output.xlsx')
    merged.to_excel(writer,'Sheet7')
    writer.save()


messagebox.showinfo(title="Congrats", message="Comparison results saved to ouput.xlsx ")
