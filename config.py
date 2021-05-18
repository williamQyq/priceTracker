URL_INDEX = 1
NEEDQUANTITY_INDEX = 2
BUYBELOWPRICE_INDEX = 4
STATUS_INDEX = 5
PATH = r"C:\Program Files (x86)\chromedriver.exe"
filename = "Tracker_Product.xlsx"

class Config_static_user:
    #Bad practice, should encrypt private info, but whatever
    #===================================================
    f_name = "william"
    l_name = "J"
    address = ""
    city = ""
    state = ""
    zipCode = ""
    email = ""
    phone = ""
    #====================================================
    credit_card_num = ""
    expire_month = ""
    expire_year = ""
    cvv = ""
    #====================================================
    headers = {'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'}

    def __init__(self, data=None):
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
        return self.f_name
    
    def get_lname(self):
        return self.l_name
    
    def get_address(self):
        return self.address
    
    def get_city(self):
        return self.city
    
    def get_state(self):
        return self.state

    def get_zipCode(self):
        return self.zipCode
    
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
        