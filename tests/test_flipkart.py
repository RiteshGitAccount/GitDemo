from utilities.BaseClass import BaseClass
from pageObjects.FlipkartHomePage import FlipkartHomePage


class TestCaseFlipkart(BaseClass):

    def test_flipkartE2E(self):
        flipkartHomePage = FlipkartHomePage(self.driver)
        '''flipkartHomePage.ClickSearchBox()
        flipkartHomePage.EnterStringInSearchBox("Iphone 14")
        flipkartHomePage.ClickEnterStringInSearchBox()'''
        self.driver.implicitly_wait(5)
        alertText = flipkartHomePage.GetSiteName()
        assert ("Online Shopping Site" in alertText)

    def test_flipkartitemprice(self):
        flipkartHomePage = FlipkartHomePage(self.driver)
        flipkartHomePage.ClickCloseButton()
        flipkartHomePage.ClickSearchBox()
        flipkartHomePage.EnterStringInSearchBox("Monitor")
        flipkartHomePage.ClickEnterStringInSearchBox()
        self.driver.implicitly_wait(5)
        alertText = flipkartHomePage.GetItemPrice()
        print(alertText)
        assert ("50,799" in alertText)
        # flipkartHomePage.SelectItemToCart()
        # self.driver.implicitly_wait(10)
        # flipkartHomePage.ClickOnAddCart()
        # flipkartHomePage.switchWindowTAB()
        # cartItemText = flipkartHomePage.GetAddCartItemCount()
        # self.driver.implicitly_wait(10)
        # print(cartItemText)
        # alertText = flipkartHomePage.GetSiteName()
        # assert ("Online Shopping Site" in alertText)
