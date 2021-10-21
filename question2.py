import pymongo as pm
connection = pm.MongoClient('mongodb://localhost:27017/')
db = connection.obligors
list = db.obligors.find().sort([('EAD', pm.DESCENDING), ('LGD', pm.ASCENDING)]).limit(10)
for item in list:
    print(item)