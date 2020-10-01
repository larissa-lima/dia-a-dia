import pandas as pd
from pathlib import Path

#caminho dos CSV
source_files = sorted(Path('C:\Temp\MergeFIles').glob('*.csv'))

dataframes = []
for file in source_files:
    df = pd.read_csv(file) # additional arguments up to your need
    df['source'] = file.name
    dataframes.append(df)

#caminho para salvar + nome do arquivo
all = pd.concat(dataframes).to_csv("C:/Desktop/Merge Files"+"/"+"merged.csv")
