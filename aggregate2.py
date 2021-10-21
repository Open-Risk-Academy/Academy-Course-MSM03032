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
    