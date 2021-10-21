import pymongo as pm

# establish connection
connection = pm.MongoClient('mongodb://localhost:27017/')
db = connection.loandb

# for each obligor document, map the each loan's EAD to an obligor / total exposure pair
mapper = Code("""
              function() {
                  var key = this.obligor_id;
                  if(this.loans.length>0){
                      total = 0;
                      count = 0;
                      for(i=0;i<this.loans.length;i++) {
                          ead = this.loans[i].EAD;
                          total += ead;
                          count++;
                      }                 
                      emit(key, {'Loan Count': count, 'Total EAD': total});    
                  }           
                 }
              """)

reducer = Code("""
              function () {}
              """)

result = db.obligors.map_reduce(mapper, reducer, "myresults")
for doc in result.find():
    print(doc)

