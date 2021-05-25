import os
import re
import pandas as pd
from openpyxl import load_workbook

URL_INDEX = 1
NEEDQUANTITY_INDEX = 2
BUYBELOWPRICE_INDEX = 4
STATUS_INDEX = 5
filename = "Tracker_Product.xlsx"

class Config_static_user:
   
    info_dict={}
    payment_dict={}
    headers = {'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'}

    def __init__(self, data=None):
        info_tab_cols = [0,1]
        payment_tab_cols = [3,4]
        info_df = pd.read_excel(filename, sheet_name = "Config", usecols= info_tab_cols)
        payment_df = pd.read_excel(filename, sheet_name = "Config", usecols= payment_tab_cols)
   
        self.info_dict =info_df.set_index('ID').T.to_dict('list')
        self.payment_dict = payment_df.set_index('Pay ID').T.to_dict('list')
        

        if data is None:
            data={}
        else:
            self.data = data

    def get_fname(self):
       fname ="".join(self.info_dict["First name"])
       return fname

    def get_lname(self):
        lname ="".join(self.info_dict["Last name"])
        return lname
    
    def get_address(self):
        address ="".join(self.info_dict["address"])
        return address
    
    def get_city(self):
        city ="".join(self.info_dict["city"])
        return city
    
    def get_state(self):
        state ="".join(self.info_dict["state"])
        return state

    def get_zipCode(self):
        zip_code ="".join(self.info_dict["zip code"])
        return zip_code
    
    def get_email(self):
        email ="".join(self.info_dict["email"])
        return email
    
    def get_phone(self):
        phone ="".join(str(pho_num) for pho_num in self.info_dict["phone"])
        return phone
    
    def get_credit_card_number(self):
        credit_num ="".join(str(cre_num) for cre_num in self.payment_dict["credit num"])
        return credit_num

    def get_credit_card_expire_month(self):
        expire_month ="".join(self.payment_dict["expire month"])
        return expire_month

    def get_credit_card_expire_year(self):
        expire_year ="".join(self.payment_dict["expire year"])
        return expire_year
    
    def get_credit_card_cvv(self):
        cvv ="".join(self.payment_dict["cvv"])
        return cvv

    def get_account(self):
        account ="".join(self.payment_dict["account"])
        return account

    def get_account_password(self):
        password ="".join(self.payment_dict["password"])
        return password  

    def get_headers(self):
        return self.headers
    
    def get_path(self):
        cwd = os.getcwd()
        driver_path = "\chromedriver.exe"
        chrome_driver_path = cwd+driver_path
        return chrome_driver_path

        