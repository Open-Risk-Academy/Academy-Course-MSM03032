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
list = db.obligors.find().sort([('EAD', pm.DESCENDING), ('LGD', pm.ASCENDING)]).limit(10)
for item in list:
    print('ID: ', int(item['_id']))
    for key in ['EAD', 'PD', 'LGD']:
        print(key, item[key])
    print('\n')
    