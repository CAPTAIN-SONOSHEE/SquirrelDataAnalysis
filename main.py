import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = data["Primary Fur Color"] 
gray_count = len(data[fur_color == "Gray"])
cinnamon_count = len(data[fur_color == "Cinnamon"])
black_count = len(data[fur_color == "Black"])

data_dict ={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count":[gray_count, cinnamon_count, black_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
