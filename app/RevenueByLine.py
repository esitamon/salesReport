class RevenueByLine:

    def __init__(self,productName,productPrice,lotSize,quantity,discountPerProduct):
        self.productName = productName
        self.productPrice = float(productPrice)
        self.lotSize = float(lotSize)
        self.quantity = int(quantity)
        self.discountPerProduct = float(discountPerProduct)
        self.grossRevenue = self.productPrice * self.lotSize
        self.totalUnitsSold = lotSize * quantity
        self.discountedPrice = self.grossRevenue * (1- (discountPerProduct)/100)
        self.costOfDiscount = self.grossRevenue - self.discountedPrice 

    def get_product_line_revenue(self):
        return self.productName,self.grossRevenue,self.totalUnitsSold,self.costOfDiscount
    
    def __str__(self) -> str:        
        return f"Product Name:{self.productName}, Gross Revenue: {self.grossRevenue}, Total Unit Sold: {self.totalUnitsSold}, Total Unit Discount {self.costOfDiscount}"


    