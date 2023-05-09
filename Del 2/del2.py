import pandas as pd

def get_data():
    return pd.read_csv(r"data.csv", sep=",", index_col=0)

def main():
    pass

if __name__ == "__main__":
    main()