from os import error
from mypackage.fun import iterate_quests, track_instock_price
from mypackage.init import init_excel, init_chrome_driver


def main():
    try:
        try_caluse()
    except:
        print("main try except error")
    # df = init_excel('Product_Tracker.xlsx','TrackProduct')
    # driver=init_chrome_driver()
    
    # infinite = 0
    # while(infinite<1):
    #     price_reach = track_instock_price(df,driver)

    #     if price_reach:
    #         try:
    #             iterate_quests(df,driver)
    #         except: 
    #             print("failed")

    #         print("[Status]: === Finished, output result===\n")
    #     infinite+=1

    # driver.close()

def try_caluse():
    try:
        a = 100/0
        b = 100/2
        print(b)
    except:
        print("error")
    a = 100/0

main()