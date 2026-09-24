# import os
# print(os.name)
# print(os.getcwd())
# os.mkdir("new_directory")



# import datetime
# now = datetime.datetime.now()
# print(now)
# date = datetime.date(2024,1,1)
# print(date)


# import json

# data = {"name":"alice","age":25}
# json_str = json.dumps(data)
# print(json_str)

# parsed_data = json.loads(json_str)
# print(parsed_data)
# print(parsed_data["name"])
# print(parsed_data["age"])



# import numpy as np
# random_matrix = np.random.randint(1,11,size=(3,3))
# print("random 3*3 matrix:\n",random_matrix)
# matrix_sum = np.sum(random_matrix)
# print(f"\nSum of all elements: {matrix_sum}")



# import pandas as pd
# data = {'name':['alice','bob','charlie'}],
#        'age':[25,30,35],
#        'city':

# import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[10,20,15,25,30]
# plt.plot(x,y,marker="o",linestyle="-",color="b")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("simple line plot")
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.animation as animation
# fig, ax = plt.subplots()
# x= np.linspace(0,2* np.pi)



# import requests
# response = requests.get('https://api.github.com/users/octicat')
# if response = requests.


from flask import Flask
app = Flask(__namee__)
@app.route("/")
def home():
    return "hello,Flask!"
if __name__ == "__main__":
    app.rin(debug=true)
    