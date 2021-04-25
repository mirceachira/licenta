from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# !pip install git+https://github.com/trsvchn/calabar.git
# !pip3 install backtrader
# !pip3 install pyfolio
# !pip3 install tqdm
# !pip3 install wheel
# !pip3 install pandas

import datetime

# Filesystem location

# # When running in google drive
# MOUNT_LOCATION = '/content/drive'
# DATA_LOCATION = f'{MOUNT_LOCATION}/MyDrive/licenta'

# When running locally
MOUNT_LOCATION = '/root/Projects/licenta/mount/'
DATA_LOCATION = f'{MOUNT_LOCATION}'

TICKERS_LOCATION = f'{DATA_LOCATION}/tickers'
RESULTS_LOCATION = f'{DATA_LOCATION}/results'

# Email notifications
MY_EMAIL = 'chira.mircea.darius@gmail.com'
NOTIFICATION_RECEIVER_LIST = [MY_EMAIL]

# Finance API
YAHOO_FINANCE_MAX_URL = 'https://query1.finance.yahoo.com/v7/finance/download/{TICKER_NAME}?period1=946688400&period2=1609459199&interval=1d&events=history&includeAdjustedClose=true'
# 1609459199 - 2020.12.31 11:59:59 PM GMT
# 946688400 - 2000.01.01 01:00:00 AM GMT

# Tickers
TICKER_NAMES = {
#     # Gaming companies
#     'ATVI': 'Activision Blizzard, Inc.',
#     'EA': 'Electronic Arts Inc.',
#     'NTDOY': 'Nintento (traded in US)',

#     # Retail
#     'GME': 'GameStop Corp.',

#     # Tech
#     'GOOG': 'Alphabet Inc.',
# }
    # {

    # # Batch 1
    # 'MMM': '3M Company',
    # 'ABT': 'Abbott Laboratories',
    # 'ABBV': 'AbbVie Inc.',
    # 'ABMD': 'Abiomed',
    # 'ACN': 'Accenture',
    # 'ATVI': 'Activision Blizzard',
    # 'ADBE': 'Adobe Inc.',
    # 'AMD': 'Advanced Micro Devices',

    # # Batch 2
    # 'AAP': 'Advance Auto Parts',
    # 'AES': 'AES Corp',
    # 'AFL': 'Aflac',
    # 'A': 'Agilent Technologies',
    # 'APD': 'Air Products & Chemicals',
    # 'AKAM': 'Akamai Technologies',
    # 'ALK': 'Alaska Air Group',
    # 'ALB': 'Albemarle Corporation',
    # 'ARE': 'Alexandria Real Estate Equities',

    # Batch 3
    'ALXN': 'Alexion Pharmaceuticals',
    'ALGN': 'Align Technology',
    'ALLE': 'Allegion',
    'LNT': 'Alliant Energy',
    'ALL': 'Allstate Corp',
    'GOOGL': 'Alphabet Inc.',
    'GOOG': 'Alphabet Inc.',
    'MO': 'Altria Group Inc',
    'AMZN': 'Amazon.com Inc.',
    'AMCR': 'Amcor plc',

    # Batch 4
    'AEE': 'Ameren Corp',
    'AAL': 'American Airlines Group',
    'AEP': 'American Electric Power',
    'AXP': 'American Express',
    'AIG': 'American International Group',
    'AMT': 'American Tower Corp.',
    'AWK': 'American Water Works',
    'AMP': 'Ameriprise Financial',
    'ABC': 'AmerisourceBergen',
    'AME': 'Ametek',

    # Batch 5
    'AMGN': 'Amgen Inc.',
    'APH': 'Amphenol Corp',
    'ADI': 'Analog Devices, Inc.',
    'ANSS': 'ANSYS, Inc.',
    'ANTM': 'Anthem',
    'AON': 'Aon plc',
    'AOS': 'A.O. Smith Corp',
    'APA': 'APA Corporation',
    'AAPL': 'Apple Inc.',
    'AMAT': 'Applied Materials Inc.',

    # Batch 6
    'APTV': 'Aptiv PLC',
    'ADM': 'Archer-Daniels-Midland Co',
    'ANET': 'Arista Networks',
    'AJG': 'Arthur J. Gallagher & Co.',
    'AIZ': 'Assurant',
    'T': 'AT&T Inc.',
    'ATO': 'Atmos Energy',
    'ADSK': 'Autodesk Inc.',
    'ADP': 'Automatic Data Processing',
    'AZO': 'AutoZone Inc',

    # Batch 7
    'AVB': 'AvalonBay Communities',
    'AVY': 'Avery Dennison Corp',
    'BKR': 'Baker Hughes Co',
    'BLL': 'Ball Corp',
    'BAC': 'Bank of America Corp',
    'BK': 'The Bank of New York Mellon',
    'BAX': 'Baxter International Inc.',
    'BDX': 'Becton Dickinson',
    'BRK.B': 'Berkshire Hathaway',
    'BBY': 'Best Buy Co. Inc.',

    # Batch 8
    'BIO': 'Bio-Rad Laboratories',
    'BIIB': 'Biogen Inc.',
    'BLK': 'BlackRock',
    'BA': 'Boeing Company',
    'BKNG': 'Booking Holdings Inc',
    'BWA': 'BorgWarner',
    'BXP': 'Boston Properties',
    'BSX': 'Boston Scientific',
    'BMY': 'Bristol-Myers Squibb',
    'AVGO': 'Broadcom Inc.',

    # Batch 9
    # 'BR': 'Broadridge Financial Solutions',
    # 'BF.B': 'Brown-Forman Corp.',
    # 'CHRW': 'C. H. Robinson Worldwide',
    # 'COG': 'Cabot Oil & Gas',
    # 'CDNS': 'Cadence Design Systems',
    # 'CZR': 'Caesars Entertainment',
    # 'CPB': 'Campbell Soup',
    # 'COF': 'Capital One Financial',
    # 'CAH': 'Cardinal Health Inc.',
    # 'KMX': 'Carmax Inc',
    # 'CCL': 'Carnival Corp.',
    # 'CARR': 'Carrier Global',
    # 'CTLT': 'Catalent',
    # 'CAT': 'Caterpillar Inc.',
    # 'CBOE': 'Cboe Global Markets',
    # 'CBRE': 'CBRE Group',
    # 'CDW': 'CDW',
    # 'CE': 'Celanese',
    # 'CNC': 'Centene Corporation',
    # 'CNP': 'CenterPoint Energy',
    # 'CERN': 'Cerner',
    # 'CF': 'CF Industries Holdings Inc',
    # 'SCHW': 'Charles Schwab Corporation',
    # 'CHTR': 'Charter Communications',
    # 'CVX': 'Chevron Corp.',
    # 'CMG': 'Chipotle Mexican Grill',
    # 'CB': 'Chubb Limited',
    # 'CHD': 'Church & Dwight',
    # 'CI': 'Cigna',
    # 'CINF': 'Cincinnati Financial',
    # 'CTAS': 'Cintas Corporation',
    # 'CSCO': 'Cisco Systems',
    # 'C': 'Citigroup Inc.',
    # 'CFG': 'Citizens Financial Group',
    # 'CTXS': 'Citrix Systems',
    # 'CLX': 'The Clorox Company',
    # 'CME': 'CME Group Inc.',
    # 'CMS': 'CMS Energy',
    # 'KO': 'Coca-Cola Company',
    # 'CTSH': 'Cognizant Technology Solutions',
    # 'CL': 'Colgate-Palmolive',
    # 'CMCSA': 'Comcast Corp.',
    # 'CMA': 'Comerica Inc.',
    # 'CAG': 'Conagra Brands',
    # 'COP': 'ConocoPhillips',
    # 'ED': 'Consolidated Edison',
    # 'STZ': 'Constellation Brands',
    # 'COO': 'The Cooper Companies',
    # 'CPRT': 'Copart Inc',
    # 'GLW': 'Corning Inc.',
    # 'CTVA': 'Corteva',
    # 'COST': 'Costco Wholesale Corp.',
    # 'CCI': 'Crown Castle',
    # 'CSX': 'CSX Corp.',
    # 'CMI': 'Cummins Inc.',
    # 'CVS': 'CVS Health',
    # 'DHI': 'D. R. Horton',
    # 'DHR': 'Danaher Corp.',
    # 'DRI': 'Darden Restaurants',
    # 'DVA': 'DaVita Inc.',
    # 'DE': 'Deere & Co.',
    # 'DAL': 'Delta Air Lines Inc.',
    # 'XRAY': 'Dentsply Sirona',
    # 'DVN': 'Devon Energy',
    # 'DXCM': 'DexCom',
    # 'FANG': 'Diamondback Energy',
    # 'DLR': 'Digital Realty Trust Inc',
    # 'DFS': 'Discover Financial Services',
    # 'DISCA': 'Discovery, Inc.',
    # 'DISCK': 'Discovery, Inc.',
    # 'DISH': 'Dish Network',
    # 'DG': 'Dollar General',
    # 'DLTR': 'Dollar Tree',
    # 'D': 'Dominion Energy',
    # 'DPZ': "Domino's Pizza",
    # 'DOV': 'Dover Corporation',
    # 'DOW': 'Dow Inc.',
    # 'DTE': 'DTE Energy Co.',
    # 'DUK': 'Duke Energy',
    # 'DRE': 'Duke Realty Corp',
    # 'DD': 'DuPont de Nemours Inc',
    # 'DXC': 'DXC Technology',
    # 'EMN': 'Eastman Chemical',
    # 'ETN': 'Eaton Corporation',
    # 'EBAY': 'eBay Inc.',
    # 'ECL': 'Ecolab Inc.',
    # 'EIX': "Edison Int'l",
    # 'EW': 'Edwards Lifesciences',
    # 'EA': 'Electronic Arts',
    # 'EMR': 'Emerson Electric Company',
    # 'ENPH': 'Enphase Energy',
    # 'ETR': 'Entergy Corp.',
    # 'EOG': 'EOG Resources',
    # 'EFX': 'Equifax Inc.',
    # 'EQIX': 'Equinix',
    # 'EQR': 'Equity Residential',
    # 'ESS': 'Essex Property Trust, Inc.',
    # 'EL': 'Estée Lauder Companies',
    # 'ETSY': 'Etsy',
    # 'EVRG': 'Evergy',
    # 'ES': 'Eversource Energy',
    # 'RE': 'Everest Re Group Ltd.',
    # 'EXC': 'Exelon Corp.',
    # 'EXPE': 'Expedia Group',
    # 'EXPD': 'Expeditors',
    # 'EXR': 'Extra Space Storage',
    # 'XOM': 'Exxon Mobil Corp.',
    # 'FFIV': 'F5 Networks',
    # 'FB': 'Facebook, Inc.',
    # 'FAST': 'Fastenal Co',
    # 'FRT': 'Federal Realty Investment Trust',
    # 'FDX': 'FedEx Corporation',
    # 'FIS': 'Fidelity National Information Services',
    # 'FITB': 'Fifth Third Bancorp',
    # 'FE': 'FirstEnergy Corp',
    # 'FRC': 'First Republic Bank',
    # 'FISV': 'Fiserv Inc',
    # 'FLT': 'FleetCor Technologies Inc',
    # 'FLIR': 'FLIR Systems',
    # 'FMC': 'FMC Corporation',
    # 'F': 'Ford Motor Company',
    # 'FTNT': 'Fortinet',
    # 'FTV': 'Fortive Corp',
    # 'FBHS': 'Fortune Brands Home & Security',
    # 'FOXA': 'Fox Corporation',
    # 'FOX': 'Fox Corporation',
    # 'BEN': 'Franklin Resources',
    # 'FCX': 'Freeport-McMoRan Inc.',
    # 'GPS': 'Gap Inc.',
    # 'GRMN': 'Garmin Ltd.',
    # 'IT': 'Gartner Inc',
    # 'GNRC': 'Generac Holdings',
    # 'GD': 'General Dynamics',
    # 'GE': 'General Electric',
    # 'GIS': 'General Mills',
    # 'GM': 'General Motors',
    # 'GPC': 'Genuine Parts',
    # 'GILD': 'Gilead Sciences',
    # 'GL': 'Globe Life Inc.',
    # 'GPN': 'Global Payments Inc.',
    # 'GS': 'Goldman Sachs Group',
    # 'GWW': 'Grainger (W.W.) Inc.',
    # 'HAL': 'Halliburton Co.',
    # 'HBI': 'Hanesbrands Inc',
    # 'HIG': 'Hartford Financial Svc.Gp.',
    # 'HAS': 'Hasbro Inc.',
    # 'HCA': 'HCA Healthcare',
    # 'PEAK': 'Healthpeak Properties',
    # 'HSIC': 'Henry Schein',
    # 'HSY': 'The Hershey Company',
    # 'HES': 'Hess Corporation',
    # 'HPE': 'Hewlett Packard Enterprise',
    # 'HLT': 'Hilton Worldwide Holdings Inc',
    # 'HFC': 'HollyFrontier Corp',
    # 'HOLX': 'Hologic',
    # 'HD': 'Home Depot',
    # 'HON': "Honeywell Int'l Inc.",
    # 'HRL': 'Hormel Foods Corp.',
    # 'HST': 'Host Hotels & Resorts',
    # 'HWM': 'Howmet Aerospace',
    # 'HPQ': 'HP Inc.',
    # 'HUM': 'Humana Inc.',
    # 'HBAN': 'Huntington Bancshares',
    # 'HII': 'Huntington Ingalls Industries',
    # 'IEX': 'IDEX Corporation',
    # 'IDXX': 'Idexx Laboratories',
    # 'INFO': 'IHS Markit',
    # 'ITW': 'Illinois Tool Works',
    # 'ILMN': 'Illumina Inc',
    # 'INCY': 'Incyte',
    # 'IR': 'Ingersoll-Rand',
    # 'INTC': 'Intel Corp.',
    # 'ICE': 'Intercontinental Exchange',
    # 'IBM': 'International Business Machines',
    # 'IP': 'International Paper',
    # 'IPG': 'Interpublic Group',
    # 'IFF': 'International Flavors & Fragrances',
    # 'INTU': 'Intuit Inc.',
    # 'ISRG': 'Intuitive Surgical Inc.',
    # 'IVZ': 'Invesco Ltd.',
    # 'IPGP': 'IPG Photonics Corp.',
    # 'IQV': 'IQVIA Holdings Inc.',
    # 'IRM': 'Iron Mountain Incorporated',
    # 'JKHY': 'Jack Henry & Associates',
    # 'J': 'Jacobs Engineering Group',
    # 'JBHT': 'J. B. Hunt Transport Services',
    # 'SJM': 'JM Smucker',
    # 'JNJ': 'Johnson & Johnson',
    # 'JCI': 'Johnson Controls International',
    # 'JPM': 'JPMorgan Chase & Co.',
    # 'JNPR': 'Juniper Networks',
    # 'KSU': 'Kansas City Southern',
    # 'K': 'Kellogg Co.',
    # 'KEY': 'KeyCorp',
    # 'KEYS': 'Keysight Technologies',
    # 'KMB': 'Kimberly-Clark',
    # 'KIM': 'Kimco Realty',
    # 'KMI': 'Kinder Morgan',
    # 'KLAC': 'KLA Corporation',
    # 'KHC': 'Kraft Heinz Co',
    # 'KR': 'Kroger Co.',
    # 'LB': 'L Brands Inc.',
    # 'LHX': 'L3Harris Technologies',
    # 'LH': 'Laboratory Corp. of America Holding',
    # 'LRCX': 'Lam Research',
    # 'LW': 'Lamb Weston Holdings Inc',
    # 'LVS': 'Las Vegas Sands',
    # 'LEG': 'Leggett & Platt',
    # 'LDOS': 'Leidos Holdings',
    # 'LEN': 'Lennar Corp.',
    # 'LLY': 'Lilly (Eli) & Co.',
    # 'LNC': 'Lincoln National',
    # 'LIN': 'Linde plc',
    # 'LYV': 'Live Nation Entertainment',
    # 'LKQ': 'LKQ Corporation',
    # 'LMT': 'Lockheed Martin Corp.',
    # 'L': 'Loews Corp.',
    # 'LOW': "Lowe's Cos.",
    # 'LUMN': 'Lumen Technologies',
    # 'LYB': 'LyondellBasell',
    # 'MTB': 'M&T Bank',
    # 'MRO': 'Marathon Oil Corp.',
    # 'MPC': 'Marathon Petroleum',
    # 'MKTX': 'MarketAxess',
    # 'MAR': 'Marriott International',
    # 'MMC': 'Marsh & McLennan',
    # 'MLM': 'Martin Marietta Materials',
    # 'MAS': 'Masco Corp.',
    # 'MA': 'Mastercard Inc.',
    # 'MKC': 'McCormick & Co.',
    # 'MXIM': 'Maxim Integrated Products',
    # 'MCD': "McDonald's Corp.",
    # 'MCK': 'McKesson Corp.',
    # 'MDT': 'Medtronic plc',
    # 'MRK': 'Merck & Co.',
    # 'MET': 'MetLife Inc.',
    # 'MTD': 'Mettler Toledo',
    # 'MGM': 'MGM Resorts International',
    # 'MCHP': 'Microchip Technology',
    # 'MU': 'Micron Technology',
    # 'MSFT': 'Microsoft Corp.',
    # 'MAA': 'Mid-America Apartments',
    # 'MHK': 'Mohawk Industries',
    # 'TAP': 'Molson Coors Beverage Company',
    # 'MDLZ': 'Mondelez International',
    # 'MPWR': 'Monolithic Power Systems',
    # 'MNST': 'Monster Beverage',
    # 'MCO': "Moody's Corp",
    # 'MS': 'Morgan Stanley',
    # 'MOS': 'The Mosaic Company',
    # 'MSI': 'Motorola Solutions Inc.',
    # 'MSCI': 'MSCI Inc',
    # 'NDAQ': 'Nasdaq, Inc.',
    # 'NTAP': 'NetApp',
    # 'NFLX': 'Netflix Inc.',
    # 'NWL': 'Newell Brands',
    # 'NEM': 'Newmont Corporation',
    # 'NWSA': 'News Corp',
    # 'NWS': 'News Corp',
    # 'NEE': 'NextEra Energy',
    # 'NLSN': 'Nielsen Holdings',
    # 'NKE': 'Nike, Inc.',
    # 'NI': 'NiSource Inc.',
    # 'NSC': 'Norfolk Southern Corp.',
    # 'NTRS': 'Northern Trust Corp.',
    # 'NOC': 'Northrop Grumman',
    # 'NLOK': 'NortonLifeLock',
    # 'NCLH': 'Norwegian Cruise Line Holdings',
    # 'NOV': 'NOV Inc.',
    # 'NRG': 'NRG Energy',
    # 'NUE': 'Nucor Corp.',
    # 'NVDA': 'Nvidia Corporation',
    # 'NVR': 'NVR, Inc.',
    # 'NXPI': 'NXP Semiconductors',
    # 'ORLY': "O'Reilly Automotive",
    # 'OXY': 'Occidental Petroleum',
    # 'ODFL': 'Old Dominion Freight Line',
    # 'OMC': 'Omnicom Group',
    # 'OKE': 'Oneok',
    # 'ORCL': 'Oracle Corp.',
    # 'OTIS': 'Otis Worldwide',
    # 'PCAR': 'Paccar',
    # 'PKG': 'Packaging Corporation of America',
    # 'PH': 'Parker-Hannifin',
    # 'PAYX': 'Paychex Inc.',
    # 'PAYC': 'Paycom',
    # 'PYPL': 'PayPal',
    # 'PENN': 'Penn National Gaming',
    # 'PNR': 'Pentair plc',
    # 'PBCT': "People's United Financial",
    # 'PEP': 'PepsiCo Inc.',
    # 'PKI': 'PerkinElmer',
    # 'PRGO': 'Perrigo',
    # 'PFE': 'Pfizer Inc.',
    # 'PM': 'Philip Morris International',
    # 'PSX': 'Phillips 66',
    # 'PNW': 'Pinnacle West Capital',
    # 'PXD': 'Pioneer Natural Resources',
    # 'PNC': 'PNC Financial Services',
    # 'POOL': 'Pool Corporation',
    # 'PPG': 'PPG Industries',
    # 'PPL': 'PPL Corp.',
    # 'PFG': 'Principal Financial Group',
    # 'PG': 'Procter & Gamble',
    # 'PGR': 'Progressive Corp.',
    # 'PLD': 'Prologis',
    # 'PRU': 'Prudential Financial',
    # 'PTC': 'PTC Inc',
    # 'PEG': 'Public Service Enterprise Group (PSEG)',
    # 'PSA': 'Public Storage',
    # 'PHM': 'PulteGroup',
    # 'PVH': 'PVH Corp.',
    # 'QRVO': 'Qorvo',
    # 'PWR': 'Quanta Services Inc.',
    # 'QCOM': 'Qualcomm',
    # 'DGX': 'Quest Diagnostics',
    # 'RL': 'Ralph Lauren Corporation',
    # 'RJF': 'Raymond James Financial',
    # 'RTX': 'Raytheon Technologies',
    # 'O': 'Realty Income Corporation',
    # 'REG': 'Regency Centers Corporation',
    # 'REGN': 'Regeneron Pharmaceuticals',
    # 'RF': 'Regions Financial Corp.',
    # 'RSG': 'Republic Services Inc',
    # 'RMD': 'ResMed',
    # 'RHI': 'Robert Half International',
    # 'ROK': 'Rockwell Automation Inc.',
    # 'ROL': 'Rollins, Inc.',
    # 'ROP': 'Roper Technologies',
    # 'ROST': 'Ross Stores',
    # 'RCL': 'Royal Caribbean Group',
    # 'SPGI': 'S&P Global Inc.',
    # 'CRM': 'Salesforce.com',
    # 'SBAC': 'SBA Communications',
    # 'SLB': 'Schlumberger Ltd.',
    # 'STX': 'Seagate Technology',
    # 'SEE': 'Sealed Air',
    # 'SRE': 'Sempra Energy',
    # 'NOW': 'ServiceNow',
    # 'SHW': 'Sherwin-Williams',
    # 'SPG': 'Simon Property Group Inc',
    # 'SWKS': 'Skyworks Solutions',
    # 'SNA': 'Snap-on',
    # 'SO': 'Southern Company',
    # 'LUV': 'Southwest Airlines',
    # 'SWK': 'Stanley Black & Decker',
    # 'SBUX': 'Starbucks Corp.',
    # 'STT': 'State Street Corp.',
    # 'STE': 'Steris',
    # 'SYK': 'Stryker Corp.',
    # 'SIVB': 'SVB Financial',
    # 'SYF': 'Synchrony Financial',
    # 'SNPS': 'Synopsys Inc.',
    # 'SYY': 'Sysco Corp.',
    # 'TMUS': 'T-Mobile US',
    # 'TROW': 'T. Rowe Price Group',
    # 'TTWO': 'Take-Two Interactive',
    # 'TPR': 'Tapestry, Inc.',
    # 'TGT': 'Target Corp.',
    # 'TEL': 'TE Connectivity Ltd.',
    # 'TDY': 'Teledyne Technologies',
    # 'TFX': 'Teleflex',
    # 'TER': 'Teradyne',
    # 'TSLA': 'Tesla, Inc.',
    # 'TXN': 'Texas Instruments',
    # 'TXT': 'Textron Inc.',
    # 'TMO': 'Thermo Fisher Scientific',
    # 'TJX': 'TJX Companies Inc.',
    # 'TSCO': 'Tractor Supply Company',
    # 'TT': 'Trane Technologies plc',
    # 'TDG': 'TransDigm Group',
    # 'TRV': 'The Travelers Companies',
    # 'TRMB': 'Trimble Inc.',
    # 'TFC': 'Truist Financial',
    # 'TWTR': 'Twitter, Inc.',
    # 'TYL': 'Tyler Technologies',
    # 'TSN': 'Tyson Foods',
    # 'UDR': 'UDR, Inc.',
    # 'ULTA': 'Ulta Beauty',
    # 'USB': 'U.S. Bancorp',
    # 'UAA': 'Under Armour',
    # 'UA': 'Under Armour',
    # 'UNP': 'Union Pacific Corp',
    # 'UAL': 'United Airlines Holdings',
    # 'UNH': 'UnitedHealth Group Inc.',
    # 'UPS': 'United Parcel Service',
    # 'URI': 'United Rentals, Inc.',
    # 'UHS': 'Universal Health Services',
    # 'UNM': 'Unum Group',
    # 'VLO': 'Valero Energy',
    # 'VTR': 'Ventas Inc',
    # 'VRSN': 'Verisign Inc.',
    # 'VRSK': 'Verisk Analytics',
    # 'VZ': 'Verizon Communications',
    # 'VRTX': 'Vertex Pharmaceuticals Inc',
    # 'VFC': 'VF Corporation',
    # 'VIAC': 'ViacomCBS',
    # 'VTRS': 'Viatris',
    # 'V': 'Visa Inc.',
    # 'VNO': 'Vornado Realty Trust',
    # 'VMC': 'Vulcan Materials',
    # 'WRB': 'W. R. Berkley Corporation',
    # 'WAB': 'Westinghouse Air Brake Technologies Corp',
    # 'WMT': 'Walmart',
    # 'WBA': 'Walgreens Boots Alliance',
    # 'DIS': 'The Walt Disney Company',
    # 'WM': 'Waste Management Inc.',
    # 'WAT': 'Waters Corporation',
    # 'WEC': 'WEC Energy Group',
    # 'WFC': 'Wells Fargo',
    # 'WELL': 'Welltower Inc.',
    # 'WST': 'West Pharmaceutical Services',
    # 'WDC': 'Western Digital',
    # 'WU': 'Western Union Co',
    # 'WRK': 'WestRock',
    # 'WY': 'Weyerhaeuser',
    # 'WHR': 'Whirlpool Corp.',
    # 'WMB': 'Williams Companies',
    # 'WLTW': 'Willis Towers Watson',
    # 'WYNN': 'Wynn Resorts Ltd',
    # 'XEL': 'Xcel Energy Inc',
    # 'XLNX': 'Xilinx',
    # 'XYL': 'Xylem Inc.',
    # 'YUM': 'Yum! Brands Inc',
    # 'ZBRA': 'Zebra Technologies',
    # 'ZBH': 'Zimmer Biomet',
    # 'ZION': 'Zions Bancorp',
    # 'ZTS': 'Zoetis'
}

TICKERS = list(TICKER_NAMES.keys())

# Strategy defaults
DEFAULT_FROM_DATE = datetime.datetime(2018, 1, 1)
DEFAULT_TO_DATE = datetime.datetime(2020, 12, 31)
DEFAULT_CASH = 1000.0
DEFAULT_COMMISION = 0.0
DEFAULT_CPU_COUNT = 8

# Some other configs
KLASS_KEY = 'klass'
RESULTS_FILENAME = 'results'


import datetime
import os.path
import sys
import uuid
import copy
import warnings

import pandas as pd
import requests
import tqdm
import backtrader as bt
import pyfolio as pf


warnings.filterwarnings('ignore')

def add_entry_to_csv(csv_filename, trade_info_dict):
    csv_path = f'{RESULTS_LOCATION}/{csv_filename}.csv'

    trade_info_dict = {k: [v] for k, v in trade_info_dict.items()}

    trade_df = pd.DataFrame.from_dict(trade_info_dict)
    trade_df.to_csv(csv_path, mode='a', index=False, header=False)

def get_ticker_csv_path(ticker_name):
  return f'{TICKERS_LOCATION}/{ticker_name}.csv'


def get_ticker_csv_as_df(ticker_name):
    return pd.read_csv(get_ticker_csv_path(ticker_name))


def download_latest_ticker_csv(ticker_name):
    yahoo_url = YAHOO_FINANCE_MAX_URL.format(TICKER_NAME=ticker_name)
    file_respone = requests.get(yahoo_url)

    csv_path = get_ticker_csv_path(ticker_name)

    with open(csv_path, 'wb') as f:
        f.write(file_respone.content)


def update_all_ticker_csvs():
    with tqdm.tqdm(total=len(TICKERS)) as pbar:
        for ticker_name in TICKERS:
            download_latest_ticker_csv(ticker_name)
            pbar.update(1)

# update_all_ticker_csvs()
# download_latest_ticker_csv('GOOG')

def bt_opt_callback(cb):
    pbar.update()

def test_strategy(strategy_class, ticker_name, from_date=DEFAULT_FROM_DATE, to_date=DEFAULT_TO_DATE, cash=DEFAULT_CASH, commision=DEFAULT_COMMISION, cpu_count=DEFAULT_CPU_COUNT, **strategy_kwargs):
    # Create a cerebro entity
    cerebro = bt.Cerebro()
    kwargs = {
        'ticker': ticker_name,
        **strategy_kwargs
    }

    # Add a strategy
    strats = cerebro.optstrategy(
        strategy_class,
        **kwargs
      )

    # Create a Data Feed
    data = bt.feeds.YahooFinanceCSVData(
        dataname=get_ticker_csv_path(ticker_name),
        # Do not pass values before this date
        fromdate=from_date,
        # Do not pass values before this date
        todate=to_date,
        # Do not pass values after this date
        reverse=False
    )

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # Set our desired cash start
    cerebro.broker.setcash(cash)

    # Add pyfolio analyzer for stats
    cerebro.addanalyzer(bt.analyzers.PyFolio, _name='pyfolio')

    # Add a FixedSize sizer according to the stake
    cerebro.addsizer(bt.sizers.FixedSize, stake=10)

    # Set the commission
    cerebro.broker.setcommission(commission=commision)

    cerebro.optcallback(cb=bt_opt_callback)

    # Run over everything
    cerebro.run(maxcpus=cpu_count)

import time

def run_through_tickers(strategy_class, ticker_list, *args, **kwargs):
    for ticker_name in ticker_list:
        test_strategy(strategy_class, ticker_name, *args, **kwargs)


def run_backtest_for_strategy_by_name(strategy_name, ticker_list=TICKERS):
    print(f'Running `run_backtest_for_strategy_by_name` for {strategy_name} for {len(ticker_list)} tickers')
    strategy_setup = copy.deepcopy(STRATEGIES_ALL_CONFIGS)[strategy_name]
    strategy_klass = strategy_setup.pop(KLASS_KEY)
    return run_backtest_for_strategy(strategy_klass, ticker_list, strategy_setup)


def list_configs(configs):
    """Translate a configuration with ranges into a list of dicts with value pairs"""
    config_dict_list = [{'_dummy_param': 1}]

    for name, value in configs.items():
        if type(value) == range:
            new_config_dict_list = []
            for v in value:
                for cd in config_dict_list:
                   new_config_dict_list.append({
                       name: v,
                       **cd
                   })
            config_dict_list = new_config_dict_list
        else:
            new_config_dict_list = []
            for cd in config_dict_list:
                new_config_dict_list.append({
                    name: value,
                    **cd
                })
            config_dict_list = new_config_dict_list

    for x in config_dict_list:
        x.pop('_dummy_param')

    return config_dict_list


def run_backtest_for_strategy(strategy_klass, ticker_list, configs):
    config_combination_list = list_configs(copy.deepcopy(configs))

    total_nr_jobs = len(ticker_list) * len(config_combination_list)


    run_through_tickers(strategy_klass, ticker_list, **configs)


def run_backtest_for_strategy_for_all_tickers(strategy_klass, configs):
    return run_backtest_for_strategy(strategy_klass, TICKERS, configs)

class RaynerTeoStrategy(bt.Strategy):
    """
    Rayner Teo Strategy with some additional logging

    Market:
      any stock

    Define the trend:
      (closing?) price above the 200-day moving average

    Entry:
      10-period RSI below 30 (buy on the next day's open)

    Exit:
      10-period RSI above 40, or after 10 trading days (sell on the next day's open)
    """
    params = (
            # TODO: these should be in a defaults class or something maybe
            # SMA
            ('maperiod', 15),

            # RSI
            ('rsi_open_period', 10),
            ('rsi_close_period', 30),

            # ADX
            ('adx_period', 14),

            # PPO
            ('ppo_period_short', 12),
            ('ppo_period_long', 26),

            # Stochastic
            ('stochastic_period', 14),

            # Other
            ('days_ago_close_period', 10),
            ('printlog', False),
            ('ticker', 'GME'),
        )

    def log(self, txt, dt=None, doprint=False):
        ''' Logging function for this strategy'''
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close

        # To keep track of pending orders and buy price/commission
        self.order = None
        self.buyprice = None
        self.buycomm = None

        # Add a MovingAverageSimple indicator
        self.sma = bt.indicators.SimpleMovingAverage(
            self.datas[0],
            period=self.params.maperiod
        )
        self.rsi = bt.indicators.RSI(period=self.params.rsi_open_period)
        self.adx = bt.indicators.ADX(period=self.params.adx_period)
        self.ppo = bt.indicators.PPO(
            period1=self.params.ppo_period_short,
            period2=self.params.ppo_period_long
        ) # , period_signal=?)
        self.stochastic = bt.indicators.Stochastic(period=self.params.stochastic_period)
        # TODO: There are other parameters here, add them all or as needed!

        self.order_placed_days_ago = 0
        self.csv_filename = RESULTS_FILENAME

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Sell
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Write down: no pending order
        self.order = None


    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])

        # Check if an order is pending ... if yes, we cannot send a 2nd one
        if self.order:
            return
        from datetime import datetime

        # Check if we are in the market
        if not self.position:

            # Not yet ... we MIGHT BUY if ...
            if self.dataclose[0] > self.sma[0] and self.rsi[0] < 30:
                # BUY, BUY, BUY!!! (with all possible default parameters)
                self.log('BUY CREATE, %.2f' % self.dataclose[0])

                self.trade_info_dict = {
                    'uid': str(uuid.uuid1()),
                    'ticker': self.params.ticker,
                    'date': self.data.datetime.date(),
                    'price_open': self.dataclose[0],
                    'adx': self.adx[0],
                    'ppo': self.ppo[0],
                    'stochastic': self.stochastic[0],
                    'maperiod': self.params.maperiod,
                    'rsi_open_period': self.params.rsi_open_period,
                    'rsi_close_period': self.params.rsi_close_period,
                    'adx_period': self.params.adx_period,
                    'ppo_period_short': self.params.ppo_period_short,
                    'ppo_period_long': self.params.ppo_period_long,
                    'stochastic_period': self.params.stochastic_period,
                    'days_ago_close_period': self.params.days_ago_close_period,
                }

                # CONSIDERATION: the 'checked' price vs the 'order accepted at' price

                # Keep track of the created order to avoid a 2nd order
                self.order = self.buy()
        else:
            if self.rsi[0] > self.params.rsi_close_period or self.order_placed_days_ago == self.params.days_ago_close_period:
                # SELL, SELL, SELL!!! (with all possible default parameters)
                self.log('SELL CREATE, %.2f' % self.dataclose[0])

                # Keep track of the created order to avoid a 2nd order
                self.order = self.sell()

                # Log the selling price
                self.trade_info_dict['price_sell'] = self.dataclose[0]
                add_entry_to_csv(csv_filename=self.csv_filename, trade_info_dict=copy.deepcopy(self.trade_info_dict))

                self.order_placed_days_ago = 0
            else:
                self.order_placed_days_ago += 1

    def stop(self):
        self.log(
            f'(MA Period {self.params.maperiod}, '
            f'RSI open {self.params.rsi_open_period}, '
            f'RSI close {self.params.rsi_close_period}, '
            f'Close after {self.params.days_ago_close_period} days) '
            f'Ending Value {self.broker.getvalue()}',
            doprint=False
        )

STRATEGIES_ALL_CONFIGS = {
    'Rayner Teo High Winrate': {
        KLASS_KEY: RaynerTeoStrategy,

        # Optimization
        'maperiod': range(150, 300, 25),
        'rsi_open_period': range(6, 16, 2),
        'rsi_close_period': range(26, 36, 2),
        'days_ago_close_period': range(8, 13)

        # # Dummy run
        # 'maperiod': 256,
        # 'rsi_open_period': 8,
        # 'rsi_close_period': 32,
        # 'days_ago_close_period': 8
    },
}

from tqdm.auto import tqdm

strategy_name = 'Rayner Teo High Winrate'

cfg_cpy = copy.deepcopy(STRATEGIES_ALL_CONFIGS[strategy_name])
cfg_cpy.pop(KLASS_KEY)
cfg_list = list_configs(cfg_cpy)
expected_number_of_tests = len(cfg_list) * len(TICKERS)

pbar = tqdm(desc='Running backtests', leave=True, position=1, unit='run', colour='violet', total=expected_number_of_tests)
resulting_GME_df = run_backtest_for_strategy_by_name('Rayner Teo High Winrate')

# !ls mount/results

# !cat mount/results/main.csv | wc -l

# !shuf -n 10 mount/results/main.csv

# !rm mount/results/results.csv
