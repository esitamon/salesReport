class Sale:
    
    def __init__(self,id,productId,teamId,quantity,discount):
        self.id = id
        self.productId = productId
        self.teamId = teamId
        self.quantity = quantity
        self.discount = discount

    def __str__(self):
        return f"Sale ID: {self.id}, Product ID: {self.productId}, Team ID: {self.teamId}, Quantity: {self.quantity}, Discount: {self.discount}"
    
    def __eq__(self,other):
        if isinstance(other,Sale):
            return self.id == other.i
        else:
            return False
    
    def __hash__(self):
        return hash(self.id)
    def getSaleId(self):
        return self.id
    def getProductId(self):
        return self.productId
    def getTeamId(self):
        return self.teamId
    def getQuantity(self):
        return self.quantity    
    def getDiscount(self):
        return self.discount
    

