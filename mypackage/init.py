from mypackage.module import pd, pathlib, config
from mypackage.module import pd,webdriver,Options

def init_excel(spreadsheet,sheet):
    sprdsheet_path = pathlib.Path(__file__).parent.parent.absolute().joinpath(spreadsheet)
    prod_tracker = pd.read_excel(sprdsheet_path, sheet)
    df = pd.DataFrame(prod_tracker)
    print(df)
    return df


def init_chrome_driver():
    user_agent = config.Config_static_user()
    user_agent_headers = user_agent.get_headers()

    chrome_options = Options() 
    chrome_options.add_experimental_option("detach",True)
    chrome_options.add_argument(f'user-agent={user_agent_headers}')
    driver = webdriver.Chrome(executable_path=user_agent.get_path(), options=chrome_options)

    
    print(f"[User Agent: \n{driver.execute_script('return navigator.userAgent;')}\n\n")

    return driver