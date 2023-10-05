import time


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight); return document.body.scrollHeight")
        lastCount = pageLength
        match = False

        while match == False:
            time.sleep(2)
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight); return document.body.scrollHeight")

            if lastCount == pageLength:
                match = True
            lastCount = pageLength
            time.sleep(2)

