import pandas as pd

def clean_csv(file_path, output_path):
    df = pd.read_csv(file_path)

    df.columns = df.columns.str.strip()

    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

    df.to_csv(output_path, index=False)