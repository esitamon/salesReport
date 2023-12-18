import csv

class FileLoader:
    def __init__(self,team_file,product_file,sale_file):
        self.team_file = team_file
        self.product_file = product_file
        self.sale_file = sale_file
        self.team = []
        self.product = []
        self.sales = []
        self.print(".......Initializing report data.........")
  

    def __load_team(self):
        pass
    def __load_product(self):
        pass
    def __load_sale(self):
        pass

    def load_all(self):
        self.team = self.__load_team()
        self.product= self.__load_product()
        self.sales = self.__load_sale()
        self.print(f"........All data loaded........")

    def print(self,msg):
        print(f"{msg}")

    def get_products(self):
        return self.product
    
    def get_sales(self):
        return self.sales
    
    def get_team(self):
        return self.team
    

