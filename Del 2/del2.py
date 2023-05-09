import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

def get_data():
    return pd.read_csv(r"data.csv", sep=",", index_col=0)

def main():
    data = get_data()
    d = {}
    
    for index, row in data.iterrows():
        if d.__contains__(datetime.strptime(row.name, '%Y-%m-%d').year):
            continue
        
        if row["Betula"] > 0:
            d[datetime.strptime(row.name, '%Y-%m-%d').year] = row["Day of year"]
    
    plt.scatter(d.keys(), d.values())
    
    plt.xlabel("Year")
    plt.ylabel("Day of year")
    plt.title("Pollen")
    plt.show()

if __name__ == "__main__":
    main()