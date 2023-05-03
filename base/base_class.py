class Base():
    def __init__(self, driver):
        self.driver = driver


    """Method get current url""" #метод,возвращающий наш url

    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url " + get_url)