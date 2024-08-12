import pandas
import csv


with open("weather.csv") as data_file:
    data = csv.reader(data_file)
#     data = data_file.readlines()
    temperatures = []
    for row in data:
        if row[0] != 'Day':
            temperatures.append(int(row[1]))

p_data = pandas.read_csv("weather.csv")
#print(p_data["Temperature"].max())
dict_data = p_data.to_dict()
#print(dict_data)

p_data.to_excel("weather.xlsx")

#print(type(p_data))
#print(type(p_data["Weather"]))

#print(p_data["Weather"].to_string())

# l_data = p_data["Temperature"].to_list()
# print(round(sum(l_data)/ len(l_data), 1))

#print(round(p_data["Temperature"].max(), 1))
highest_temp = p_data["Temperature"].max()

#print(p_data[p_data.Temperature == highest_temp])

monday = p_data[p_data.Day == 'Monday']
#print(str(int((monday["Temperature"] * (9/5)) +32)) + "F")

data_dict = {
    "names" : ["terry", "elizabeth", "george"],
    "year_of_birth" : [1984,1986,2015]
}

d_frame = pandas.DataFrame(data_dict)
d_frame.to_csv("years_of_births.csv")
print(d_frame)