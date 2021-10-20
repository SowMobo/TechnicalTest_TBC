from ebaysdk.finding import Connection as find_connect
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# get inputs from user
def getItems(api_id, keyword):
    # deal with acces to eBay developper API
    api = find_connect(appid = api_id, config_file = None)
    
    # Extract data fron eBay
    api_request = {'keywords' : keyword, 'outputSelector':'SellerInfo',
        'paginationInput': {'entriesPerPage': 100,'pageNumber': 1}}
        
    response = api.execute('findItemsByKeywords', api_request)
    soup = BeautifulSoup(response.content, 'lxml')

    totalentries = int(soup.find('totalentries').text)
    items = soup.find_all('item')
    #  give feedback to the user about his request
    print("Successfully list of {} extracted!".format(keyword))
    # return list of items founded
    return items
    

# Write items to indicaded google spreadsheet file
def writeItemsToSpreadsheet(jsonFileName, items, sheetName):
    #deal with acces to google spreadsheet API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonFileName)
    gc = gspread.authorize(credentials)

    # open our spreedsheet
    wks = gc.open(sheetName).sheet1
    wks.clear()
    
    header = ['category', 'title', 'price', 'url', 'seller', 'listingtype', 'condition']
    wks.append_row(header)
    
    for item in items:
        cat= item.categoryname.string.lower()
        title = item.title.string.lower().strip()
        price = int(round(float(item.currentprice.string)))
        url = item.viewitemurl.string.lower()
        seller = item.sellerusername.text.lower()
        listingtype = item.listingtype.string.lower()
        condition = item.conditiondisplayname.string.lower()
        wks.append_row([cat, title, price, url, seller, listingtype, condition])
    
