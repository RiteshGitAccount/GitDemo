import pytest

from selenium.webdriver import Keys

from selenium.webdriver.common.by import By


class FlipkartHomePage:

    def __init__(self, driver):
        self.driver = driver

    searchBox = (By.XPATH, "//input[@class='_3704LK']")
    searchButton = (By.XPATH, "//button[@type='submit']")
    thirdItemPrice = (By.XPATH, "(//div[@class='_30jeq3 _1_WHN1'])[3]")
    closeButton = (By.XPATH, "//button[@class='_2KpZ6l _2doB4z']")
    getSiteName = (By.XPATH, "//img[@title='Flipkart']")
    getListOfItems = (By.XPATH, "//div[@class='_4rR01T']")
    getItems = (By.XPATH, "(//div[@class='_4rR01T'])[2]")
    getItemPrice = (By.XPATH, "(//div[@class='_30jeq3 _1_WHN1'])[2]")
    # getItems = (By.XPATH, ("(//textarea[contains(@class,'form-control ')])["\" + b + "\"]")
    # getItems = (By.XPATH, ((By.xpath("//*[@text=\"" + text + "\"]"))
    clickAddCart = (By.XPATH, "//button[@class='_2KpZ6l _2U9uOA _3v1-ww']")
    cartAddItemCount = (By.XPATH, "//div[@class='KK-o3G']")
    logInButton = (By.XPATH, "//a[@class ='_1_3w1N']")

    def GetItemPrice(self):
        return self.driver.find_element(*FlipkartHomePage.getItemPrice).text
        # print(content.text)

    # print(content.get_attribute("innerHTML"))

    def ClickOnLogInButton(self):
        return self.driver.find_element(*FlipkartHomePage.logInButton).click()

    def ClickSearchBox(self):
        return self.driver.find_element(*FlipkartHomePage.searchBox).click()

    def EnterStringInSearchBox(self, stringPhone):
        return self.driver.find_element(*FlipkartHomePage.searchBox).send_keys(stringPhone)

    def ClickOnSearchButton(self):
        return self.driver.find_element(*FlipkartHomePage.searchButton).click()

    def GetItemValue(self):
        returnvalue = self.driver.find_element(*FlipkartHomePage.thirdItemPrice).text
        return returnvalue

    def GetAddCartItemCount(self):
        returnvalue = self.driver.find_element(*FlipkartHomePage.cartAddItemCount).text
        return returnvalue

    def ClickCloseButton(self):
        return self.driver.find_element(*FlipkartHomePage.closeButton).click()

    def ClickEnterStringInSearchBox(self):
        return self.driver.find_element(*FlipkartHomePage.searchBox).send_keys(Keys.ENTER)

    def GetSiteName(self):
        # print(self.driver.title)
        return self.driver.title

    def GetListOfItems(self, stringItemName, getListOfItems=None):
        requiredItem = []
        self.driver.find_elements(getListOfItems)
        for stringItemName in getListOfItems:
            requiredItem.append(stringItemName.text)
            return requiredItem

    def SelectItemToCart(self):
        return self.driver.find_element(*FlipkartHomePage.getItems).click()

    def ClickOnAddCart(self):
        return self.driver.find_element(*FlipkartHomePage.clickAddCart).click()

    def switchWindowTAB(self):
        windowOpened = self.driver.window_handles
        self.driver.switch_to.window(windowOpened[1])
