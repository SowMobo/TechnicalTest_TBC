import sys
import click

from ebaysdk.finding import Connection as find_connect
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from funcModule import getItems
from funcModule import writeItemsToSpreadsheet

@click.command()

def main():
    # get the name of item to find and the user ebay API ID
    keyword = input('Enter the name of  item you are looking for :\n')
    api_id = input('Enter eBay ID (note:you should sign in to get it):\n')
    
    # scrap ebay and extract items
    items = getItems(api_id, keyword)
    
    # get json file (credentials) and the name of spreadsheet you want to write to
    jsonFileName = input('Enter the name of json file that contains the client_email information:\n')
    sheetName = input('Enter the name of spreadsheet file you want to write to:\n')
    
    # Write items to indicaded google spreadsheet file
    writeItemsToSpreadsheet(jsonFileName, items, sheetName)
    
if __name__ == '__main__':
    main()
