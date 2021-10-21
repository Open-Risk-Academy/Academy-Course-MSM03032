function createLoans() {
    for (var i = 1; i <= 20; i++) {
        // construct loan data
        EAD = Math.random()
        LGD = Math.random()
        // assign loan randomly to some obligor
        j = Math.floor(Math.random() * 10)
        // insert loan document
        db.loans.insert(
            {
                "loan_id": i,
                "owner": j,
                "EAD": EAD,
                "LGD": LGD
            }
        )
    }
}
