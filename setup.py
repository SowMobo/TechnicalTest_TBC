from setuptools import setup, find_packages

setup(
    name = 'eBay_scraping',
    version = '0.0.0',
    packages = find_packages(),
    install_requirements = [
        'clicl',
        'ebaysdk',
        'beautifulsoup4',
        'gspread',
        'oauth2clien'],
    entry_points = '''
        [console_scripts]
            eBay_scraping = main:main
     '''
     )
