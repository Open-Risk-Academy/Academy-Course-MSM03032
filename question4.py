import pymongo as pm
connection = pm.MongoClient('mongodb://localhost:27017/')
db = connection.obligors
query = {'_id': 100001}
update = {'$set': {"EAD": 0.9} }
db.obligors.find_and_modify(query, update)
print(db.obligors.find_one({'_id': 100001}))
