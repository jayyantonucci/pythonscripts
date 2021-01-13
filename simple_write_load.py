import pickle 

#create variable
var = 'hello world'
print(var)

#write variable to file
pickle.dump(var, open('file_name.dat', 'wb'))

#change variable
var = 'goodbye'
print(var)

#load variable
var = pickle.load(open('file_name.dat', 'rb'))
print(var)
