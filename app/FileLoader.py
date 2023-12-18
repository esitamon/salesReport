import csv
from Team import Team
from Product import Product
from pathlib import Path
from Sale import Sale

class FileLoader:
    def __init__(self, team_file, product_file, sale_file):
        self.team_file = team_file
        self.product_file = product_file
        self.sale_file = sale_file
        self.teams = []
        self.products = []
        self.sales = []
        self.print(".......Initializing report data.........\n")

    def load_team(self):
        print(f"Loading teams from '{self.team_file}'...\n")
        try:
            with open(self.team_file, newline='', encoding='utf-8-sig') as file:
                csv_reader = csv.DictReader(file)
                self.teams = [Team(row['TeamID'], row['Name']) for row in csv_reader]
                for team in self.teams:
                    print(team)
                print("\n")
                return self.teams
        except FileNotFoundError:
            print(f"Error: File '{self.team_file}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    def load_product(self):
        print(f"Loading products from '{self.product_file}'...\n")
        try:
            with open(self.product_file, newline='', encoding='utf-8-sig') as file:
                csv_reader = csv.reader(file, delimiter=',', quotechar='"')
                self.products = [Product(*row) for row in csv_reader]
                for product in self.products:
                    print(product)
                print("\n")
                return self.products
        except FileNotFoundError:
            print(f"Error: File '{self.product_file}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    def load_sale(self):
        print(f"Loading sales from '{self.sale_file}'...\n")
        try:
            with open(self.sale_file, newline='', encoding='utf-8-sig') as file:
                csv_reader = csv.reader(file, delimiter=',', quotechar='"')
                self.sales = [Sale(*row) for row in csv_reader]
                for sale in self.sales:
                    print(sale)
                print("\n")
                return self.sales
        except FileNotFoundError:
            print(f"Error: File '{self.sale_file}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    def load_all(self):
        self.teams = self.load_team()
        self.products = self.load_product()
        self.sales = self.load_sale()
        self.print(f"........All data loaded........")

    def print(self, msg):
        print(f"{msg}")

    def get_products(self):
        return self.products

    def get_sales(self):
        return self.sales

    def get_team(self):
        return self.teams
