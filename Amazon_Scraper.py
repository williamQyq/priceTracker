import requests
from glob import glob
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from time import sleep
import winsound

# http://www.networkinghowtos.com/howto/common-user-agent-list/
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


def search_product_list(interval_count = 1, interval_sec = 600):
    prod_tracker = pd.read_csv('trackers/TRACKER_PRODUCTS.csv', sep=';')
    prod_tracker_URLS = prod_tracker.url
    tracker_log = pd.DataFrame()
    
    interval = 0 # counter reset
    frequency = 350
    duration = 50

    while True:
        now = datetime.now().strftime('%Y-%m-%d %Hh%Mm')

        for x, url in enumerate(prod_tracker_URLS):
            page = requests.get(url, headers=HEADERS)
            soup = BeautifulSoup(page.content, features="lxml")

            # #Amazon block scraper use SP-API https://github.com/amzn/selling-partner-api-docs
            # try:
            #     #product title
            #     title_html = soup.find("span", id='productTitle')
            #     title = title_html.get_text().strip()
            #     price = float(soup.find("span", id='price_inside_buybox').get_text().replace('$','').strip())

            # except:
            #     title = ''
            #     price = ''

            # try:
            #     review_score = float(soup.select('i[class*="a-icon a-icon-star a-star-"]')[0].get_text().split(' ')[0].replace(",", "."))
            #     review_count = int(soup.select('#acrCustomerReviewText')[0].get_text().split(' ')[0].replace(".", ""))
            # except:
            #     # sometimes review_score is in a different position... had to add this alternative with another try statement
            #     try:
            #         review_score = float(soup.select('i[class*="a-icon a-icon-star a-star-"]')[1].get_text().split(' ')[0].replace(",", "."))
            #         review_count = int(soup.select('#acrCustomerReviewText')[0].get_text().split(' ')[0].replace(".", ""))
            #     except:
            #         review_score = ''
            #         review_count = ''
            
            # # checking if there is "Out of stock"
            # try:
            #     soup.select('#availability .a-color-state')[0].get_text().strip()
            #     stock = 'Out of Stock'
            # except:
            #     # checking if there is "Out of stock" on a second possible position
            #     try:
            #         soup.select('#availability .a-color-price')[0].get_text().strip()
            #         stock = 'Out of Stock'
            #     except:
            #         # if there is any error in the previous try statements, it means the product is available
            #         stock = 'Available'
            
            #Bestbuy 
            try:
                title_html = soup.find("h1", ["heading-5","v-fw-regular"])
                title = title_html.get_text().strip()
                price_div = soup.find("div", ["priceView-hero-price", "priceView-customer-price"])
                price = float(price_div.find("span").get_text().replace('$','').strip())

            except:
                title = ''
                price = ''

            log = pd.DataFrame({'date': now.replace('h',':').replace('m',''),
                                'code': prod_tracker.code[x], # this code comes from the TRACKER_PRODUCTS file
                                'url': url,
                                'title': title,
                                'buy_below': prod_tracker.buy_below[x], # this price comes from the TRACKER_PRODUCTS file
                                'price': price,
                                # 'stock': stock,
                                # 'review_score': review_score,
                                # 'review_count': review_count
                                }, index=[x])
            try:
                # This is where you can integrate an email alert!
                if price < prod_tracker.buy_below[x]:
                    print('************************ ALERT! Buy the '+prod_tracker.code[x]+" $"+str(price)+' ************************')
                    for i in range(0,20):
                        winsound.Beep(frequency, duration)
                        frequency+= 50
            except:
                # sometimes we don't get any price, so there will be an error in the if condition above
                pass

            tracker_log = tracker_log.append(log)
            print('appended '+ prod_tracker.code[x] +'\n' + title + '\n'+str(price)+'\n')            
            sleep(3)
        
        interval += 1# counter update
        sleep(interval_sec)
        # print('end of interval '+ str(interval))

        # after the run, checks last search history record, and appends this run results to it, saving a new file
        last_search = glob('D:/William/price_scraper_proj/amazon_webscraper-master/search_history/*.xlsx')[-1] # path to file in the folder
        search_hist = pd.read_excel(last_search)
        final_df = search_hist.append(tracker_log, sort=False)

        final_df.to_excel('search_history/SEARCH_HISTORY_{}.xlsx'.format(now), index=False)

        #reset sound frequency
        frequency = 250
        duration = 100
        print('end of search')

search_product_list()
