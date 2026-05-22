from abc import ABC, abstractmethod
from case_study.scraper.constants import DataStoreConstants
from typing import List
from pydantic import BaseModel


class BaseDataStore(ABC):
    data_store = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abstractmethod
    def save(self, data: List[BaseModel], *args, **kwargs):
        """
        Save the data to the data store.
        """
        raise NotImplementedError


class GoogleSheetsDataStore(BaseDataStore):
    data_store = DataStoreConstants.GOOGLE_SHEETS

    def save(self, data: List[BaseModel], *args, **kwargs):
        # Logic to save data to Google Sheets
        pass


class DynamoDBDataStore(BaseDataStore):
    data_store = DataStoreConstants.DYNAMODB

    def save(self, data: List[BaseModel], *args, **kwargs):
        # Logic to save data to DynamoDB
        pass


class BigQueryDataStore(BaseDataStore):
    data_store = DataStoreConstants.BIGQUERY

    def save(self, data: List[BaseModel], *args, **kwargs):
        # Logic to save data to BigQuery
        pass


class DataStoreFactory:
    @staticmethod
    def create_data_store(data_store_type: str) -> BaseDataStore:
        """
        Factory method to create a data store instance based on the type.
        """
        if data_store_type == DataStoreConstants.GOOGLE_SHEETS:
            return GoogleSheetsDataStore()
        elif data_store_type == DataStoreConstants.DYNAMODB:
            return DynamoDBDataStore()
        elif data_store_type == DataStoreConstants.BIGQUERY:
            return BigQueryDataStore()
        else:
            raise ValueError(f"Unsupported data store type: {data_store_type}")
