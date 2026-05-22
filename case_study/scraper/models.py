from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Type


class OutputModelV1(BaseModel):
    platform: str
    scraped_at: datetime
    user_id: Optional[str]
    user_name: Optional[str]
    review_added_at: datetime
    review_text: Optional[str]
    review_rating: Optional[int]
    review_title: Optional[str]
    review_url: Optional[str]
    review_language: Optional[str]
    review_helpfulness: Optional[int]
    review_verified: Optional[bool]


class OutputModelFactory:
    @staticmethod
    def create_output_model(version: str) -> Type[BaseModel]:
        if version == "v1":
            return OutputModelV1
        else:
            raise ValueError(f"Unsupported version: {version}")
