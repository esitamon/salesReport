class Product:
    def __init__(self,productId,productName,productPrice,lotSize):
        self.productId=productId
        self.productName=productName
        self.productPrice=float(productPrice)
        self.lotSize=int(lotSize)
        
    def __str__(self):
        return f"productId: {self.productId},productName: {self.productName},productPrice: {self.productPrice},lotSize: {self.lotSize}"
    
    def __eq__(self,other):

        if isinstance(other,Product):
            return self.productId == other.productI
        else:
            return False
        
    def __hash__(self):
        return hash(self.productId)
    
    def getProductId(self):
        return self.productId
    def getProductName(self):
        return self.productName
    def getProductPrice(self):
        return self.productPrice
    def getLotSize(self):
        return self.lotSize
    