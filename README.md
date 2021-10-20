This project use a simple CLI struture to:
1- Collect a list of product via an python-eBay developper APi through filters and paginations
2- Write the list to google spreedsheet
3- Share the project via a git link

------------Scraping eBay to extract a list of item-------------------------------
To do that, first I install ebaysdk and BeautifulSoup4 PACKAGES and then I create an ebay developper api account to get my api ID (this take a working day to be available)

----------- Write the list of item to google spreadsheet project----------------------
First, I need to install gspread and oauth2client PACKAGES. Second, I create a service account key and that generates a .json file that contains a client_email which I use share my spreadsheet with.


-----------------------How to run the app-------------------------------------------------
From commande line (Terminal) type eBay_scraping and follow the sequence:
1- type the name of the item your are searching for from ebay web site
2- type your eBay App ID (Client ID). 
3- type the name of your json file you generate from google comsole developper (note: you should enable google sheet API and google drive API)
4- type the name of your spreedsheet file you set up on your google cloud

                            see the results --)
