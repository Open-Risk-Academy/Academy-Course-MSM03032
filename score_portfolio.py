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
import numpy as np

# establish connection
connection = pm.MongoClient('mongodb://localhost:27017/')
db = connection.loandb

# for each obligor document extract the relevant financials into python lists
values = []
obligor_id = []
for doc in db.obligors.find():
    obligor_id.append(doc['obligor_id'])
    values.append([doc['financials']['ST Debt'], 
                   doc['financials']['LT Debt'],
                   doc['financials']['Equity'],
                   doc['financials']['Debt Service'],
                   doc['financials']['Net Profit']])
# store the data into a numpy array
raw_values = np.array(values)    
# manipulate columns
# add 1 to 2 and divide by 3
# divide 4 by 5

# derive model characteristic
debt = raw_values[:,0] + raw_values[:,1]
equity = raw_values[:,2]
leverage = debt / equity
dscr = raw_values[:,4] / raw_values[:,3]

# stored scorecard (variables)
scorecard = np.array([0.5, 0.5])

# compute score values and rating score
score_values = np.column_stack((leverage,dscr))
rating_score = np.dot(score_values, scorecard)

# compute probability of default
offset = 5.0
t1 = 1.0 + np.exp(offset - rating_score)
pd = np.true_divide(1.0,t1)