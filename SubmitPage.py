from selenium.webdriver.common.by import By


class SubmitPage:

    def __init__(self, driver):
        self.driver = driver

    Name = (By.NAME, "name")
    Email = (By.NAME, "email")
    Password = (By.ID, "exampleInputPassword1")
    LoveIceCreams = (By.XPATH, "//input[@id='exampleCheck1']")
    Gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    Status = (By.CLASS_NAME, "form-check-inline")
    Birth = (By.NAME, "bday")
    Submit = (By.XPATH, "//input[@type='submit']")
    SuccessMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def getName(self):
        return self.driver.find_element(*SubmitPage.Name)

    def getEmail(self):
        return self.driver.find_element(*SubmitPage.Email)

    def getPassword(self):
        return self.driver.find_element(*SubmitPage.Password)

    def getLoveIceCreams(self):
        return self.driver.find_element(*SubmitPage.LoveIceCreams)

    def getGender(self):
        return self.driver.find_element(*SubmitPage.Gender)

    def getStatus(self):
        return self.driver.find_elements(*SubmitPage.Status)

    def getBirth(self):
        return self.driver.find_element(*SubmitPage.Birth)

    def getSubmit(self):
        return self.driver.find_element(*SubmitPage.Submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*SubmitPage.SuccessMessage)
