import pickle

with open("cookies.pickle",'rb') as file:
    data = pickle.load(file)

c = 1
for i in data:
    print(i)
    c+=1
