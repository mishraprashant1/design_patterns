from abc import ABC, abstractmethod
from case_study.scraper.constants import PlatformsConstants
from case_study.scraper.models import OutputModelFactory
from typing import Type
from pydantic import BaseModel


class BaseAdapter(ABC):
    """
    Base class for adapters.
    """
    _output_model = None
    _output_model_version = "v1"
    _output = None

    def __init__(self, *args, **kwargs):
        self._output_model = OutputModelFactory.create_output_model(self._output_model_version)

    @abstractmethod
    def adapt(self, data: dict, *args, **kwargs) -> Type[BaseModel]:
        """
        Adapt the data to the desired format.
        """
        raise NotImplementedError

    def _validate_data(self, model: Type[BaseModel]):
        """
        Validate the data against the output model.
        """
        return self._output_model.model_validate(model)

    def process(self, data: dict, *args, **kwargs) -> BaseModel:
        """
        Process the data through the adapter.
        """
        self._output = self.adapt(data, *args, **kwargs)
        self._output = self._validate_data(self._output)
        return self._output


class QuoraAdapter(BaseAdapter):
    """
    Adapter for Quora.
    """
    _output_model = PlatformsConstants.QUORA

    def adapt(self, data: dict, *args, **kwargs) -> Type[BaseModel]:
        # Logic to adapt Quora data
        return self._output_model(**data)


class RedditAdapter(BaseAdapter):
    """
    Adapter for Reddit.
    """
    _output_model = PlatformsConstants.REDDIT

    def adapt(self, data: dict, *args, **kwargs) -> Type[BaseModel]:
        # Logic to adapt Reddit data
        return self._output_model(**data)


class TrustpilotAdapter(BaseAdapter):
    """
    Adapter for Trustpilot.
    """
    _output_model = PlatformsConstants.TRUSTPILOT

    def adapt(self, data: dict, *args, **kwargs) -> Type[BaseModel]:
        # Logic to adapt Trustpilot data
        return self._output_model(**data)


class AdapterFactory:
    """
    Factory class to create adapter instances.
    """

    @staticmethod
    def create_adapter(adapter_type, *args, **kwargs) -> BaseAdapter:
        if adapter_type == PlatformsConstants.QUORA:
            return QuoraAdapter(*args, **kwargs)
        elif adapter_type == PlatformsConstants.REDDIT:
            return RedditAdapter(*args, **kwargs)
        elif adapter_type == PlatformsConstants.TRUSTPILOT:
            return TrustpilotAdapter(*args, **kwargs)
        else:
            raise ValueError(f"Unsupported adapter type: {adapter_type}")
