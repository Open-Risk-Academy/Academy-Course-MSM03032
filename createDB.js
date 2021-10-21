function createDB() {
	db.createCollection("obligors");
	
	// iterate over the number of obligors
	for(var i=1; i <=10; i++)  {
		
		// construct random obligor data
		PD = Math.random()
		turnover = Math.random()
		equity = Math.random()
		st_debt = Math.random()
		lt_debt = Math.random()
		debt_service = Math.random()
		ebitda = Math.random()
		net_profit = Math.random()
		employees = Math.random()	

                // random number of loans (can also be zero)	
		loan_number = Math.floor(Math.random()  * 5)
		loans = []

		for(var j=1; j <= loan_number; j++)  {
		      // construct loan data
		      EAD = Math.random()	
		      LGD = Math.random()	
		      loans.push( {'ID': j, 'EAD' : EAD, 'LGD': LGD})
	        }
		
		// insert collateral info
		collateral = []
		if (loan_number > 0) {
			 coll_number = Math.floor(Math.random()  * 2)
			 for(var k=1; k<=coll_number; k++) {
				value = Math.random()
				collateral.push('ID': k, {'value': value} )
                         }				 
		}
		
		// insert obligor document		
		db.obligors.insert(
			{"obligor_id": i,
			"PD": PD,	
			"financials": {
				"Turnover": turnover,
				"Equity": equity,
				"ST Debt": st_debt,
				"LT Debt": lt_debt,
				"Debt Service": debt_service,
				"EBITDA": ebitda,
				"Net Profit": net_profit,
				"Employees": employees		
			},
                        "loans": loans,
			"collateral": collateral
		}) 		
	}
}
