import time

import pytest
from selenium.webdriver.common.by import By

from Data import Data
from BaseClass import BaseClass
from SubmitPage import SubmitPage


class TestOne(BaseClass):

    #@pytest.fixture
    #def getData(self):
    #    return Data.getTestData("VALID")

    @pytest.fixture(params=Data.getTestData("VALID")+Data.getTestData("NOEMAIL"))
    def getData(self, request):
        return request.param
    #@pytest.mark.parametrize("getData",Data.getTestData("VALID")+Data.getTestData("NOEMAIL"),ids=["testValid1","testValid2","testValid3"])
    def testValid(self,getData):
        log = self.getlogger()
        log.info(getData)
        print(getData)
        submitPage = SubmitPage(self.driver)
        submitPage.getName().send_keys(getData["Name"])

        submitPage.getEmail().send_keys(getData["Email"])
        submitPage.getPassword().send_keys(getData["Password"])
        submitPage.getLoveIceCreams().click()
        self.selectOptionByText(submitPage.getGender(),getData["Gender"])
        options = submitPage.getStatus()
        for option in options:
            if option.find_element(By.TAG_NAME,"label").text == getData["Status"]:
                option.find_element(By.TAG_NAME,"input").click()
                break
        submitPage.getBirth().send_keys(getData["Birth"])
        submitPage.getSubmit().click()
        assert("Success" in submitPage.getSuccessMessage().text)

        self.driver.refresh()


"""
    @pytest.mark.parametrize("data", [getData("EMPTY")], ids=["testEmpty"])
    def testEmpty(self,data):
        pass

    @pytest.mark.parametrize("data", [getData("NOEMAIL")], ids=["testNoemail"])
    def testNoemail(self,data):
        pass

"""

