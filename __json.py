import json

#json module allowed us to convert between 
# json and python object


#==========object python to json================
data1 = {"name":"jose","name":"daniel"}
dataJson = json.dumps(data1)
print(dataJson)


#==========json object to python================
data2 = '{"name":"pedro","name":"maria"}'
dataPython = json.loads(data2)
print(dataPython)