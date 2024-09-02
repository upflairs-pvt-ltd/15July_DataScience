from pymongo import MongoClient 
connection_string= "mongodb+srv://divya7413:LKQOuBg5DRvBBoaE@jmd.q3tz0.mongodb.net/?retryWrites=true&w=majority&appName=JMD"
client = MongoClient(connection_string)
database = client['Farmer2']
collection = database['FarmerData1']

documents = collection.find()  # select * from table;
for document in documents: 
    print(document) 
print("thank you!") 

# execute this file to fectch your data from database 
