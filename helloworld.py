from pymongo import MongoClient
db = MongoClient('mongodb://localhost:27017/')
print(db.database_names())

db.test.insert_many([{'i': i} for i in xrange(10000)]).inserted_ids
db.test.count()

bulk = db.test.initialize_ordered_bulk_op()
bulk.find({}).remove()
bulk.insert({'_id': 1})
bulk.insert({'_id': 2})
bulk.insert({'_id': 3})
bulk.find({'_id': 1}).update({'$set': {'foo': 'bar'}})
bulk.find({'_id': 4}).upsert().update({'$inc': {'j': 1}})
bulk.find({'j': 1}).replace_one({'j': 2})