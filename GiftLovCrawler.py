from bs4 import Tag
from WebCrawler import WebCrawler
import urllib

"""
GiftLovCrawler class is serving the purpose of scrapping/printing Gift cards code(s).
"""

class GiftLovCrawler(WebCrawler):
    
    apiURL = 'https://distribution.giftlov.com/api/Orders/'
    
    crawledRoutes = [
        #'95ccc5cc-dec2-480f-a0b9-37233c064133/49f5520479158e085a8d10000cc7740a0834bbde49493a0493415cae2a57ad6a/o/15642927',
        '78a01bfa-b803-4ccd-8f99-5de87bfbc8a7/669f317a91995af3a8fb6d5cf6cec4066033bc8ca4e305d19b5d1229c461a3f9/o/13188160'
    ]

    def formatGiftCode(self, elements: Tag) -> str:
        return str(elements[0].renderContents().decode("utf-8"))
    
    def tokenizer(self):
        import os
        from selenium import webdriver

        from selenium.webdriver.chrome.options import Options 
        
        # instance of Options class allows 
        # us to configure Headless Chrome 
        options = Options() 
        
        # this parameter tells Chrome that 
        # it should be run without UI (Headless) 
        options.headless = True
        
        # initializing webdriver for Chrome with our options 
        driver = webdriver.Chrome(options=options) 
        """
        jsCode = '<script src="https://www.google.com/recaptcha/api.js?render=6LdEQXceAAAAAAdO88phAYq-xPLg2RkaEVEDgHd2"></script>'
        jsCode = jsCode + '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>'
        jsCode = jsCode + '<script type="text/javascript">'
        jsCode = jsCode + 'grecaptcha.ready(function () {'
        jsCode = jsCode + '    grecaptcha.execute("6LdEQXceAAAAAAdO88phAYq-xPLg2RkaEVEDgHd2", { action: "submit" }).then(function (token) {'
        jsCode = jsCode + 'alert(token)'
        jsCode = jsCode + '    });'
        jsCode = jsCode + '});'
        jsCode = jsCode + '</script>'

        html = '<html><title>Temp action</title><body></body>'
        html = html + jsCode
        html = html + '</html>'
        path = os.path.abspath('sample.html')
        url = 'file://' + path
        """
        """
        with open(path, 'w') as f:
            f.write(html)
        """
        
        link = "https://www.google.com/recaptcha/api.js?render=6LdEQXceAAAAAAdO88phAYq-xPLg2RkaEVEDgHd2"
        f = urllib.request.urlopen(link)
        jsCode = f.read()
        link = "https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"
        f = urllib.request.urlopen(link)
        jsCode = jsCode + f.read()
        jsCode = jsCode.decode("utf-8") + "newToken = '';grecaptcha.ready(function () { grecaptcha.execute('6LdEQXceAAAAAAdO88phAYq-xPLg2RkaEVEDgHd2', { action: 'submit' }).then(function (token) {newToken = token }); });setTimeout(()=>{return newToken}, 6000);"

        #browser.get(url)
        
        print(driver.execute_script(jsCode))

        #browser.get
        #html = browser.page_source
        #print(html)
        #browser.quit()

    def operationCriteria(self):        
        self.tokenizer()
        return
        cardIdentifier = 'card-number'
        elements = self.elements('#' + cardIdentifier)
        if len(elements) != 0:
            print(self.formatGiftCode(elements))
            return
        elements = self.elements('.' + cardIdentifier)
        if len(elements) != 0:
            print(self.formatGiftCode(elements))
            return
        
