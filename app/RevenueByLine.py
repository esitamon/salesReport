class RevenueByLine:

    def __init__(self,productName,productPrice,lotSize,countOfSales,discountPerProduct):
        self.productName = productName
        self.productPrice = float(productPrice)
        self.lotSize = float(lotSize)
        self.countOfSales = int(countOfSales)
        self.discountPerProduct = float(discountPerProduct)
        self.grossRevenue = self.productPrice * self.lotSize * self.countOfSales
        self.totalUnitsSold = lotSize * countOfSales
        self.discountPrice = self.grossRevenue * (1- (discountPerProduct)/100)

    def get_product_line_revenue(self):
        return self.productName,self.grossRevenue,self.totalUnitsSold,self.discountPrice
    
    def __str__(self) -> str:        
        return f"Product Name:{self.productName}, Gross Revenue: {self.grossRevenue}, Total Unit Sold: {self.totalUnitsSold}, Total Unit Discount {self.discountPrice}"


    