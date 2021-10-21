import pymongo as pm
connection = pm.MongoClient('mongodb://localhost:27017/')
db = connection.obligors
last_item_id = [item for item in db.obligors.find().sort([('_id', pm.DESCENDING)]).limit(1)][0]['_id']
new_obligor = {"_id": last_item_id + 1, "EAD": 0.5, "PD": 0.2, "LGD": 0.5}
db.obligors.insert(new_obligor)
