class RevenueByTeam:
    def __init__(self,teamId,teamName,qunatitySold,productPrice,discountApplied):
        self.teamId = teamId
        self.teamName = teamName
        self.qunatitySold = qunatitySold
        self.productPrice = productPrice
        self.discountApplied = discountApplied
        self.grossRevenue = (productPrice * qunatitySold) * (1-discountApplied) 

    def get_team_revenue(self):
        return self.teamName, self.grossRevenue
    
    def __str__(self) -> str:
        return f"Team Name: {self.teamName}, Gross Revenue: {self.grossRevenue}"
    
    
    
    
