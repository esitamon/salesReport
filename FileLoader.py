import csv
from Team import Team

class FileLoader:
    def __init__(self,team_file,product_file,sale_file):
        self.team_file = team_file
        self.product_file = product_file
        self.sale_file = sale_file
        self.teams = []
        self.products = []
        self.sales = []
        self.print(".......Initializing report data.........")
  

    def __load_team(self):
        try:
            with open(self.team_file, newline='') as file:
                csv_reader =  csv.DictReader(file)
                for row in csv_reader:
                    team = Team(self.__remove_bom(row['TeamID']),row['Name'])
                    self.teams.append(team)
                    self.print(f"Team: {team.teamId} - {team.teamName}")
                for person in self.teams:
                    print(f"Team: {person.teamId} - {person.teamName}")
                return self.teams
        except FileNotFoundError:
            print(f"Error: File '{self.team_file}' not found.")
        except Exception as e:
            print(f"Error: {e.with_traceback}")

        

        
    def __load_product(self):
        pass
    def __load_sale(self):
        pass

    def __remove_bom(self,string):
        # this method removes the BOM character from the beginning of the string
        return string.replace("\ufeff", "")

    def load_all(self):
        self.teams = self.__load_team()
        self.products= self.__load_product()
        self.sales = self.__load_sale()
        self.print(f"........All data loaded........")

    def print(self,msg):
        print(f"{msg}")

    def get_products(self):
        return self.products
    
    def get_sales(self):
        return self.sales
    
    def get_team(self):
        return self.teams
    

