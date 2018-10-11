import pickle

number_of_data = int(input('Enter the  number of data : '))
data = []


for i in range(number_of_data):
    raw = input('Enter data '+str(i)+' :')
    data.append(raw)

with open('important','wb') as file:
    pickle.dump(data,file)
