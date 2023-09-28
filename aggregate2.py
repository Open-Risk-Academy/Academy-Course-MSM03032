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

# establish connection
connection = pm.MongoClient('mongodb://localhost:27017/')
db = connection.loandb

# for each obligor document, map the each loan's EAD to an obligor / total exposure pair
mapper = Code("""
              function() {
                  var key = this.obligor_id;
                  var exposures = []
                  if(this.loans.length>0){
                      for(i=0;i<this.loans.length;i++) {
                          ead = this.loans[i].EAD;
                          exposures.push(ead);
                      }                 
                      emit(key, exposures);    
                  }           
                 }
              """)

reducer = Code("""
               function (key, values) {
                 var total = 0;
                 for (var i = 0; i < values.length; i++) {
                   total += values[i];
                 }
                 return total;
               }
              """)

result = db.obligors.map_reduce(mapper, reducer, "myresults")
for doc in result.find():
    print(doc)
    