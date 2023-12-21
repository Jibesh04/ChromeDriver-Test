# pip install selenium

import unittest
from selenium import webdriver

class CrossBrowserTest(unittest.TestCase):
    def setUp(self):
        self.browsers = ["chrome", "firefox", "safari"]

    def tearDown(self):
        if hasattr(self, 'driver') and self.driver is not None:
            self.driver.quit()

    def test_cross_browser_compatibility(self):
        for browser in self.browsers:
            if browser == "chrome":
                driver = webdriver.Chrome()
            elif browser == "firefox":
                driver = webdriver.Firefox()
            elif browser == "safari":
                driver = webdriver.Safari()
            else:
                raise Exception(f"Unsupported browser: {browser}")

            try:
                driver.get("https://Jibesh04.github.io/Portfolio/")
                # assertion
                self.assertIn("Junior's Portfolio", driver.title)

            except Exception as e:
                print(f"Test failed on {browser}: {str(e)}")

            finally:
                driver.quit()

if __name__ == "__main__":
    unittest.main()
