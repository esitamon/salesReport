from Product import Product
from Sale import Sale
from Team import Team
from RevenueByLine import RevenueByLine
from RevenueByTeam import RevenueByTeam

class ReportProcessor:

    ''' This class takes the sales,teams,and products and provide methods
    to retrieve sales by team, and sales by line of produc'''

    def __init__(self,list_of_sales,list_of_teams,list_of_products):
        self.list_of_sales = list_of_sales
        self.list_of_teams = list_of_teams
        self.list_of_products = list_of_products

    def get_sales_by_team(self):
        "return the sales filters by team"
        revenueByTeam = []
        for team in self.list_of_teams:
            for sale in self.list_of_sales:
                if sale.getTeamId() == team.getTeamId():
                    teamRevenue = RevenueByTeam(team.getTeamName(),sale.getQuantity(),sale.getDiscount())   
                    print(sale)
        
    def order_in_descending_order(self):
        "return the sales in descending order"
        pass
    def order_in_ascending_order(self):
        "return the sales in ascending order"
        pass

    def get_sales_by_product_line(self):
        "return the sales filters by product and line"
        revenueByLines = []
        for product in self.list_of_products:
            for sale in self.list_of_sales:
                if sale.getProductId()    == product.getProductId():
                    revenue = RevenueByLine(product.getProductName(),product.getProductPrice(),product.getLotSize(),sale.getQuantity(),sale.getDiscount())
                    revenueByLines.append(revenue)
        for revenue in revenueByLines:
            print(revenue)
        return revenueByLines

        

