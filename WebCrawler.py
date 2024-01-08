import abc, time
import requests
from requests import Response
from bs4 import BeautifulSoup, Tag

"""
WebCrawler class is serving the purpose of scrapping formatted data
to be ready for next stage operations.
"""

class WebCrawler(object):
    __metaclass__ = abc.ABCMeta
    
    apiURL:str = ''
    """
    @apiURL:str is the API base URL used in the crawler.
    """

    crawledRoutes = []
    """
    @crawledRoutes:list is the list of routes to be operated
    if the standard crawler method was used.
    """
    
    currentPage:BeautifulSoup = None
    """
    @currentPage:BeautifulSoup this is the core scrapping object.
    """
    
    @abc.abstractmethod
    def operationCriteria(self):
        """
        This abstract method should be filled up in the next sublevel.
        It is called already in the standard 'crawl' method representing
        the main operation(s) happening in the crawler logic.
        """
        return
    
    def load(self, url: str) -> Response:
        """
        Load a given resource content.

        Args:
            url (string): resource URL to be called.

        Returns:
            (Response): resource URL content.
        """
        return requests.get(url)
    
    def HTMlParser(self, content: str):
        """
        Parse a given HTML content.

        Args:
            content (string): HTML string of a given page.
        """
        self.currentPage = BeautifulSoup(content, "html.parser")
    
    def elements(self, HTMlAttribute: str) -> Tag:
        """
        Access elements of the page based on attribute criteria.

        Args:
            HTMlAttribute (string): elements selection is based on this attribute.

        Returns:
            (Tag | None): The chosen tag(s).
        """
        return self.currentPage.select(HTMlAttribute)
    
    def crawl(self):
        """
        Run the web crawler using the operation sub-function.
        """
        for crawledRoute in self.crawledRoutes:
            response = self.load(self.apiURL + crawledRoute)
            self.HTMlParser(response.content)
            self.operationCriteria()