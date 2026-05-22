from case_study.scraper.base_scraper import ScraperFactory
from case_study.scraper.constants import PlatformsConstants, DataStoreConstants
from case_study.scraper.base_data_store import DataStoreFactory

"""

Output(Pydantic BaseModel)
    - Common output format

Scrapper
    - Quora
    - Reddit
    - Trust Pilot

Adapter
    - returns scrapper data in common Output Format
    
Data Store
    - Google Sheets
    - DynamoDB
    - BigQuery
    
    - Takes data from Adapter which is in common Output Format and stores it in the data store
"""

start_date = "2023-01-01"
end_date = "2023-01-31"
platform = PlatformsConstants.QUORA
data_store = DataStoreConstants.GOOGLE_SHEETS

scraper = ScraperFactory.create_scraper(platform, start_date, end_date)
data = scraper.scrape()

data_store = DataStoreFactory.create_data_store(data_store)
data_store.save(data)

