import os
import argparse
from FileLoader import FileLoader
from ReportProcessor import ReportProcessor

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.usage = "python report.py --team team.csv --sales sales.csv --products products.csv"
    parser.add_argument("--team", help="positional argument for loading team.csv", required=True)
    parser.add_argument("--sales", help="positional argument for loading sales.csv", required=True)
    parser.add_argument("--products", help="positional argument for loading products.csv", required=True)
    args = parser.parse_args()
    return args

def get_file_paths(args):
    cwd_path  = os.path.dirname(os.path.abspath(__file__))
    team_file = os.path.join(cwd_path, "resources", args.team)
    sales_file = os.path.join(cwd_path, "resources", args.sales)
    product_file = os.path.join(cwd_path, "resources", args.products)
    return team_file, sales_file, product_file, cwd_path

def print_file_paths(team_file, sales_file, product_file, cwd_path):
    print(f"team file: {team_file}")
    print(f"sales file: {sales_file}")
    print(f"product file: {product_file}")
    print(f"CWD Path: {cwd_path}")

def main():
    print("--------------------Starting the program------------------")

    # Parsing arguments
    args = parse_arguments()

    # Getting file paths
    team_file, sales_file, product_file, cwd_path = get_file_paths(args)

    # Print file paths
    print_file_paths(team_file, sales_file, product_file, cwd_path)

    # Load all files
    file_loader = FileLoader(team_file, product_file, sales_file)
    file_loader.load_all()

    # Run the processor to calculate report values

    sales = file_loader.get_sales()
    teams = file_loader.get_team()
    products = file_loader.get_products()
    processor = ReportProcessor(sales, teams, products)

    processor.get_sales_by_product_line()

    #processor.write_sales_by_product_report()
    #processor.write_sales_by_team_report()

if __name__ =='__main__':
    main()
