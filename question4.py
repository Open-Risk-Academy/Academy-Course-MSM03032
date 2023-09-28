"""
   Copyright 2022 - 2023 Open Risk (www.openriskmanagement.com)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import pymongo as pm
connection = pm.MongoClient('mongodb://localhost:27017/')
db = connection.obligors
query = {'_id': 100001}
update = {'$set': {"EAD": 0.9} }
db.obligors.find_and_modify(query, update)
print(db.obligors.find_one({'_id': 100001}))
