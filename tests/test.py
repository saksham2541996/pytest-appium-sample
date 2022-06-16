import pytest

@pytest.mark.usefixtures('test_setup')
class TestLink:

    def test_1(self):
        el1 = self.driver.find_element_by_id("com.lambdatest.proverbial:id/color")
        el1.click()
        return self.__class__.__name__
        
        
    def test_2(self):
        el2 = self.driver.find_element_by_id("com.lambdatest.proverbial:id/colour")
        el2.click()
        return self.__class__.__name__
        # cls = self.__class__.__name__
        # print(cls)
    



