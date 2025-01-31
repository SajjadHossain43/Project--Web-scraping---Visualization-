from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

columns = ['Brand', 'ProductName', 'DiscountedPrice', 'ActualPrice', 'Rating', 'NumberOfRatings', 'NumberOfReviews', 'SalesPackage',
            'ModelNumber', 'PartNumber', 'ModelName', 'Series', 'Color', 'Type', 'SuitableFor', 'MSOfficeProvided', 'ProcessorBrand',
              'ProcessorName', 'SSD', 'RAM', 'RAMType', 'StorageCapacity', 'GraphicProcessor', 'StorageType', 'OperatingSystem', 'USBPort',
                'Touchscreen', 'ScreenSize', 'ScreenResolution', 'ScreenType', 'Speakers', 'InternalMic', 'WirelessLAN', 'Bluetooth', 'Dimensions',
                 'Weight', 'DiskDrive', 'WebCamera', 'Keyboard', 'WarrantySummary', 'WarrantyServiceType', 'CoveredinWarranty', 
                  'NotCoveredinWarranty', 'ClockSpeed']
Contents = {}
csv_file = 'LaptopSalesData.csv'

def append_to_csv(Contents: dict, csv_file):
    list = []
    list.append(Contents)
    df = pd.DataFrame(data=list, columns=columns)
    df.to_csv(csv_file, mode='a', header=not pd.io.common.file_exists(csv_file), index=False)
    return

def prepare_data(Contents: dict, row) -> dict:
    properties = list(row.split('\n'))
    if ''.join(properties[0].split()) == 'SalesPackage':
        Contents['SalesPackage'] = properties[1]
        print(Contents['SalesPackage'])
    elif ''.join(properties[0].split()) == 'ModelNumber':
        Contents['ModelNumber'] = properties[1]
        print(Contents['ModelNumber'])
    elif ''.join(properties[0].split()) == 'PartNumber':
        Contents['PartNumber'] = properties[1]
        print(Contents['PartNumber'])
    elif ''.join(properties[0].split()) == 'PartNumber':
        Contents['PartNumber'] = properties[1]
        print(Contents['PartNumber'])
    elif ''.join(properties[0].split()) == 'ModelName':
        Contents['ModelName'] = properties[1]
        print(Contents['ModelName'])
    elif ''.join(properties[0].split()) == 'Series':
        Contents['Series'] = properties[1]
        print(Contents['Series'])
    elif ''.join(properties[0].split()) == 'Color':
        Contents['Color'] = properties[1]
        print(Contents['Color'])
    elif ''.join(properties[0].split()) == 'Type':
        Contents['Type'] = properties[1]
        print(Contents['Type'])
    elif ''.join(properties[0].split()) == 'SuitableFor':
        Contents['SuitableFor'] = properties[1]
        print(Contents['SuitableFor'])
    elif ''.join(properties[0].split()) == 'MSOfficeProvided':
        Contents['MSOfficeProvided'] = properties[1]
        print(Contents['MSOfficeProvided'])
    elif ''.join(properties[0].split()) == 'ProcessorBrand':
        Contents['ProcessorBrand'] = properties[1]
        print(Contents['ProcessorBrand'])
    elif ''.join(properties[0].split()) == 'ProcessorName':
        Contents['ProcessorName'] = properties[1]
        print(Contents['ProcessorName'])
    elif ''.join(properties[0].split()) == 'SSD':
        Contents['SSD'] = properties[1]
        print(Contents['SSD'])
    elif ''.join(properties[0].split()) == 'RAM':
        Contents['RAM'] = properties[1]
        print(Contents['RAM'])
    elif ''.join(properties[0].split()) == 'RAMType':
        Contents['RAMType'] = properties[1]
        print(Contents['RAMType'])
    elif ''.join(properties[0].split()) == 'StorageCapacity':
        Contents['StorageCapacity'] = properties[1]
        print(Contents['StorageCapacity'])
    elif ''.join(properties[0].split()) == 'GraphicProcessor':
        Contents['GraphicProcessor'] = properties[1]
        print(Contents['GraphicProcessor'])
    elif ''.join(properties[0].split()) == 'StorageType':
        Contents['StorageType'] = properties[1]
        print(Contents['StorageType'])
    elif ''.join(properties[0].split()) == 'OperatingSystem':
        Contents['OperatingSystem'] = properties[1]
        print(Contents['OperatingSystem'])
    elif ''.join(properties[0].split()) == 'USBPort':
        Contents['USBPort'] = properties[1]
        print(Contents['USBPort'])
    elif ''.join(properties[0].split()) == 'Touchscreen':
        Contents['Touchscreen'] = properties[1]
        print(Contents['Touchscreen'])
    elif ''.join(properties[0].split()) == 'ScreenSize':
        Contents['ScreenSize'] = properties[1]
        print(Contents['ScreenSize'])
    elif ''.join(properties[0].split()) == 'ScreenResolution':
        Contents['ScreenResolution'] = properties[1]
        print(Contents['ScreenResolution'])
    elif ''.join(properties[0].split()) == 'ScreenType':
        Contents['ScreenType'] = properties[1]
        print(Contents['ScreenType'])
    elif ''.join(properties[0].split()) == 'Speakers':
        Contents['Speakers'] = properties[1]
        print(Contents['Speakers'])
    elif ''.join(properties[0].split()) == 'InternalMic':
        Contents['InternalMic'] = properties[1]
        print(Contents['InternalMic'])
    elif ''.join(properties[0].split()) == 'WirelessLAN':
        Contents['WirelessLAN'] = properties[1]
        print(Contents['WirelessLAN'])
    elif ''.join(properties[0].split()) == 'Bluetooth':
        Contents['Bluetooth'] = properties[1]
        print(Contents['Bluetooth'])
    elif ''.join(properties[0].split()) == 'Dimensions':
        Contents['Dimensions'] = properties[1]
        print(Contents['Dimensions'])
    elif ''.join(properties[0].split()) == 'Weight':
        Contents['Weight'] = properties[1]
        print(Contents['Weight'])
    elif ''.join(properties[0].split()) == 'DiskDrive':
        Contents['DiskDrive'] = properties[1]
        print(Contents['DiskDrive'])
    elif ''.join(properties[0].split()) == 'WebCamera':
        Contents['WebCamera'] = properties[1]
        print(Contents['WebCamera'])
    elif ''.join(properties[0].split()) == 'Keyboard':
        Contents['Keyboard'] = properties[1]
        print(Contents['Keyboard'])
    elif ''.join(properties[0].split()) == 'WarrantySummary':
        Contents['WarrantySummary'] = properties[1]
        print(Contents['WarrantySummary'])
    elif ''.join(properties[0].split()) == 'WarrantyServiceType':
        Contents['WarrantyServiceType'] = properties[1]
        print(Contents['WarrantyServiceType'])
    elif ''.join(properties[0].split()) == 'CoveredinWarranty':
        Contents['CoveredinWarranty'] = properties[1]
        print(Contents['CoveredinWarranty'])
    elif ''.join(properties[0].split()) == 'NotCoveredinWarranty':
        Contents['NotCoveredinWarranty'] = properties[1]
        print(Contents['NotCoveredinWarranty'])
    elif ''.join(properties[0].split()) == 'ClockSpeed':
        Contents['ClockSpeed'] = properties[1]
        print(Contents['ClockSpeed'])
    return 

def scraper_engine() -> bool:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    webdriver_path = "C:\\Users\\Admin\\Downloads\\chromedriver-win64\\chromedriver.exe"
    for i in range(1, 42):
        site_url = f"https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_df6b6d84-2193-4f7e-9610-33baa9b5d33c_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop_34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=34WHNYFH5V2Y&page={i}"
        service = Service(webdriver_path)
        site_driver = webdriver.Chrome(service=service, options=chrome_options)
        site_driver.get(site_url)
        records = list(site_driver.find_elements(By.CLASS_NAME, '_75nlfW'))
        for idx, record in enumerate(records):
            try:
                product_url = record.find_element(By.CLASS_NAME, 'CGtC98').get_attribute('href')
                service = Service(webdriver_path)
                product_driver = webdriver.Chrome(service=service, options=chrome_options)
                product_driver.get(product_url)
                try:
                    Name = product_driver.find_element(By.CLASS_NAME, 'VU-ZEz').text
                    Contents['Brand'] = Name.split(' ')[0]
                    Contents['ProductName'] = Name
                except Exception:
                    Name = None
                    print('Continued from Name')
                try:
                    CurrentPrice = product_driver.find_element(By.CLASS_NAME, 'CxhGGd').text
                    Contents['DiscountedPrice'] = CurrentPrice.replace('₹', '').replace(',', '')
                except Exception:
                    CurrentPrice = None
                    print('Continued from CurrentPrice/DiscountedPrice')
                try:
                    ActualPrice = product_driver.find_element(By.CLASS_NAME, 'yRaY8j').text
                    Contents['ActualPrice'] = ActualPrice.replace('₹', '').replace(',', '')
                except Exception:
                    ActualPrice = None
                    print("Continued from ActualPrice")
                try:
                    Rating = product_driver.find_element(By.CLASS_NAME, 'XQDdHH').text
                    Contents['Rating'] = Rating
                except Exception:
                    Rating = None
                    print("Continued from Rating")
                try:
                    NumberOfRatingsReviews = product_driver.find_element(By.CLASS_NAME, 'Wphh3N').text
                    Contents['NumberOfRatings'] = NumberOfRatingsReviews.split('&')[0].strip().replace('Ratings', '').replace(',', '').strip()
                    Contents['NumberOfReviews'] = NumberOfRatingsReviews.split('&')[1].strip().replace('Reviews', '').replace(',', '').strip()
                except Exception:
                    NumberOfRatingsReviews = None
                    print("Continued from Reviews")
                print(Contents['Brand'])
                print(Contents['ProductName'])
                print(Contents['DiscountedPrice'])
                print(Contents['NumberOfRatings'])
                print(Contents['NumberOfReviews'])
                read_more_button = product_driver.find_element(By.CLASS_NAME, '_4FgsLt')
                product_driver.execute_script("arguments[0].scrollIntoView(true);", read_more_button)
                ActionChains(product_driver).move_to_element(read_more_button).perform()
                element_to_hide = product_driver.find_element(By.CLASS_NAME, "krHvwW")
                product_driver.execute_script("arguments[0].style.display = 'none';", element_to_hide)
                read_more_button.click()
                product_specs = list(product_driver.find_elements(By.CLASS_NAME, 'GNDEQ-'))
                print('start of specs . . . . .')
                for spec in product_specs:
                    table = spec.find_element(By.CLASS_NAME, '_0ZhAN9')
                    table_rows = table.find_elements(By.CLASS_NAME, 'WJdYP6')
                    for row in table_rows:
                        prepare_data(Contents, row.text)
                product_driver.quit()
                append_to_csv(Contents, csv_file)
            except Exception:
                print('error')
        site_driver.quit()
        time.sleep(3)
    return True

if __name__ == "__main__":
    print("starting...")
    print(f'sucessfully completed = {scraper_engine()}')