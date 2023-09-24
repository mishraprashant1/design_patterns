"""
The Proxy Design Pattern is a structural pattern that provides a surrogate or placeholder for another object to control
access to it. It is often used to add a level of control and management over how an object is accessed or modified.

Real-Life Example Problem:
Imagine you are building a web browser, and you want to add the functionality to load and display web pages.
Loading a web page can be a resource-intensive operation, and you want to control access to web pages to improve
performance. Additionally, you may want to log each time a page is accessed.

Solution with the Proxy Pattern:
The Proxy Pattern suggests that you create a proxy class that acts as an intermediary between the client and the real
object (the web page in this case). The proxy controls access to the real object and can add additional behavior or
checks before allowing access.
"""
from abc import ABC, abstractmethod
import requests


class WebPage(ABC):
    @abstractmethod
    def load(self):
        pass


class RealWebPage(WebPage):
    def __init__(self, url):
        self.url = url
        self.load()

    def load(self):
        print(f"Loading {self.url}")


class ProxyWebPage(WebPage):
    def __init__(self, url):
        self.url = url
        self.real_web_page = None

    def load(self):
        if self.real_web_page is None:
            self.real_web_page = RealWebPage(self.url)
        self.real_web_page.load()


if __name__ == '__main__':
    url = "https://www.google.com"
    web_page = ProxyWebPage(url)
    web_page.load()
    web_page.load()

"""
Another example of the Proxy Design Pattern is the Django ORM. When you query a model, Django does not immediately
execute the query. Instead, it creates a proxy object that acts as a placeholder for the actual results. The query is
executed only when you try to access the results. This allows Django to add additional behavior to the results, such as
caching, without modifying the original query.
"""


class FetchAPI(ABC):
    @abstractmethod
    def fetch(self):
        pass


class RealFetchAPI(FetchAPI):
    def __init__(self, url):
        self.url = url

    def fetch(self):
        print(f"Fetching {self.url}")
        response = requests.get(self.url)
        return response.json()


class ProxyFetchAPI(FetchAPI):
    def __init__(self, url):
        self.url = url
        self.api_content = None

    def fetch(self):
        if self.api_content is None:
            real_fetch_api = RealFetchAPI(self.url)
            self.api_content = real_fetch_api.fetch()
        return self.api_content


if __name__ == '__main__':
    url = "https://reqres.in/api/users?page=2"
    fetch_api = ProxyFetchAPI(url)
    print(fetch_api.fetch())
    print(fetch_api.fetch())
