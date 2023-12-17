
class ReportProcessor:

    ''' This class takes the sales,teams,and products and provide methods
    to retrieve sales by team, and sales by line of produc'''

    def __init__(self,list_of_sales,list_of_teams,list_of_products):
        self.list_of_sales = list_of_sales
        self.list_of_teams = list_of_teams
        self.list_of_products = list_of_products
        self.display_info()

    def display_info(self):
        "display the sales,teams,and products"
        print(self.list_of_sales)
        print(self.list_of_teams)
        print(self.list_of_products)

    def get_sales_by_product(self):
        "return the sales filters by type of product"
        pass
    def get_sales_by_team(self):
        "return the sales filters by team"
        pass
    def order_in_descending_order(self):
        "return the sales in descending order"
        pass
    def order_in_ascending_order(self):
        "return the sales in ascending order"
        pass
    def get_sales_by_product_and_team(self):
        "return the sales filters by product and team"
        pass
    def get_sales_by_product_and_line(self):
        "return the sales filters by product and line"
        pass

