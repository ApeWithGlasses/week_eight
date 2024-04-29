import pandas as pd
import charts as ch

def read_csv():
    df = pd.read_csv("workers.csv")
    # data, group_by, values, x_label, y_label, title, file_name
    ch.generate_bar(df, 'city', 'name', 'City', 'Workers', 'Workers per city', 'workers_per_city.png')

def run():
    read_csv()

if __name__ == "__main__":
    run()