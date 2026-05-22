from abc import ABC, abstractmethod
from case_study.scraper.base_adapter import AdapterFactory
from case_study.scraper.constants import PlatformsConstants
from case_study.scraper.models import BaseModel
from typing import List


class BasePlatformScraper(ABC):
    """
    Base class for web scrapers.
    """

    platform = None

    def __init__(self, start_date, end_date, *args, **kwargs):
        self.adapter = AdapterFactory.create_adapter(self.platform)
        self.start_date = start_date
        self.end_date = end_date

    @abstractmethod
    def scrape(self) -> List[BaseModel]:
        """
        Scrape the website and return the data.
        """
        raise NotImplementedError

    def _get_processed_data(self, data: dict, *args, **kwargs) -> BaseModel:
        """
        Process the data through the adapter.
        """
        return self.adapter.process(data, *args, **kwargs)


class QuoraScraper(BasePlatformScraper):
    """
    Scraper for Quora.
    """

    platform = PlatformsConstants.QUORA

    def __init__(self, start_date, end_date, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize any necessary attributes or clients here

    def scrape(self):
        """
        Scrape the Quora website and return the data.
        """
        # Implement the scraping logic here
        pass



class RedditScraper(BasePlatformScraper):
    """
    Scraper for Reddit.
    """

    platform = PlatformsConstants.REDDIT

    def __init__(self, start_date, end_date, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize any necessary attributes or clients here

    def scrape(self):
        """
        Scrape the Reddit website and return the data.
        """
        # Implement the scraping logic here
        pass


class TrustpilotScraper(BasePlatformScraper):
    """
    Scraper for Trustpilot.
    """

    platform = PlatformsConstants.TRUSTPILOT

    def __init__(self, start_date, end_date, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize any necessary attributes or clients here

    def scrape(self):
        """
        Scrape the Trustpilot website and return the data.
        """
        # Implement the scraping logic here
        pass


class ScraperFactory:
    """
    Factory class to create scrapers for different platforms.
    """

    @staticmethod
    def create_scraper(platform: str, *args, **kwargs) -> BasePlatformScraper:
        if platform == "quora":
            return QuoraScraper(*args, **kwargs)
        elif platform == "reddit":
            return RedditScraper(*args, **kwargs)
        elif platform == "trustpilot":
            return TrustpilotScraper(*args, **kwargs)
        else:
            raise ValueError(f"Unsupported platform: {platform}")
