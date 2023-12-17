class Sale:
    
    def __init__(self,id,productId,teamId,quantity,discount):
        self.id = id
        self.productId = productId
        self.teamId = teamId
        self.quantity = quantity
        self.discount = discount

    def __str__(self):
        return f"Sale: {self.id}, {self.productId}, {self.teamId}, {self.quantity}, {self.discount}"
    
    def __eq__(self,other):
        if isinstance(other,Sale):
            return self.id == other.i
        else:
            return False
    
    def __hash__(self):
        return hash(self.id)
    

