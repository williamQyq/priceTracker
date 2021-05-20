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
    #Bad practice, should encrypt private info, but whatever
    #===================================================
    f_name = "william"
    l_name = "J"
    address = "26 clinton drive unit 123"
    city = "Hollis"
    state = "NH"
    zipCode = "03049"
    email = "ugotexpress.act001@gmail.com"
    phone = "9788098625"
    #====================================================
    credit_card_num = "4199664858600096"
    expire_month = "06"
    expire_year = "2021"
    cvv = "111"
    #====================================================
    headers = {'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'}

    def __init__(self, data=None):
        info_tab_cols = [0,1]
        payment_tab_cols = [3,4]
        info_df = pd.read_excel(filename, sheet_name = "Config", usecols= info_tab_cols)
        payment_df = pd.read_excel(filename, sheet_name = "Config", usecols= payment_tab_cols)
   
        info_dict =info_df.set_index('ID').T.to_dict('list')
        payment_dict = payment_df.set_index('ID').T.to_dict('list')
        
        if data is None:
            data={}
        else:
            self.f_name = data['f_name']
            self.l_name = data['l_name']
            self.address = data['address']
            self.city = data['city']
            self.state = data['state']
            self.zipCode = data['zipCode']
            self.email = data['email']
            self.phone = data['phone']
            self.credit_card_num = data['credit_card_num']
            self.expire_month = data['expire_month']
            self.expire_year = data['expire_year']
            self.cvv = data['cvv']

    def get_fname(self):
        
        
        wb = load_workbook(filename)
        ws = wb.worksheets[1]
        # for col in ws.iter_cols(min_row=2,min_col = 2, max_col = 2):
        #     for cell in col:
        # print(info)
      

    def get_lname(self):
        wb = load_workbook(filename)
        ws = wb.worksheets[1]
        Info_tab = ws.tables["Info"]
        lname=ws['B3']

        return lname
    
    def get_address(self):
        wb = load_workbook(filename)
        ws = wb.worksheets[1]
        Info_tab = ws.tables["Info"]
        address=ws['B4']

        return address
    
    def get_city(self):
        wb = load_workbook(filename)
        ws = wb.worksheets[1]
        Info_tab = ws.tables["Info"]
        city=ws['B5']

        return city
    
    def get_state(self):
        wb = load_workbook(filename)
        ws = wb.worksheets[1]
        Info_tab = ws.tables["Info"]
        state=ws['B6']

        return state

    def get_zipCode(self):
        wb = load_workbook(filename)
        ws = wb.worksheets[1]
        Info_tab = ws.tables["Info"]
        fname=ws['B2']

        return fname
    
    def get_email(self):
        return self.email
    
    def get_phone(self):
        return self.phone
    
    def get_credit_card_number(self):
        return self.credit_card_num
    
    def get_credit_card_expire_month(self):
        return self.expire_month

    def get_credit_card_expire_year(self):
        return self.expire_year
    
    def get_credit_card_cvv(self):
        return self.cvv

    def get_headers(self):
        return self.headers
    
    def get_path(self):
        cwd = os.getcwd()
        driver_path = "\chromedriver.exe"
        chrome_driver_path = cwd+driver_path
        return chrome_driver_path

        