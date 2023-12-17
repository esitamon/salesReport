class FileLoader:
    def __init__(self,team_file,product_file,sale_file):
        self.team_file = team_file
        self.product_file = product_file
        self.sale_file = sale_file
        print(f"Initializing report data")

    def __load_team(self):
        pass
    def __load_product(self):
        pass
    def __load_sale(self):
        pass

    def load_all(self):
        self.__load_team()
        self.__load_product()
        self.__load_sale()
        self.print(f"All data loaded")
