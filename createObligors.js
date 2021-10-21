function createObligors() {
    for (var i = 1; i <= 10; i++) {
        // construct obligor data
        PD = Math.random()
        turnover = Math.random()
        equity = Math.random()
        st_debt = Math.random()
        lt_debt = Math.random()
        debt_service = Math.random()
        ebitda = Math.random()
        net_profit = Math.random()
        employees = Math.random()
        // insert obligor document
        db.obligors.insert(
            {
                "obligor_id": i,
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
                }
            }
        )
    }
}
