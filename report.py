import sys
import argparse
from FileLoader import FileLoader
from ReportProcessor import ReportProcessor



#setting main as the starting function
if __name__ =='__main__':
    print("--------------------Starting  the program------------------")
    #Parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="File to load")
    #load all files

    file_loader = FileLoader()
    file_loader.load_all()

    #run the processor to calculate report values
    processor = ReportProcessor(file_loader.get_sales,file_loader.get_team,file_loader.get_products)
    processor.write_sales_by_product_report()
    processor.write_sales_by_team_report()


