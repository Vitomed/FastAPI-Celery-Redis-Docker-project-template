from typing import Optional

from pydantic import BaseModel, Field, validator, root_validator


class Item(BaseModel):
    min_v: int = Field(...)
    max_v: int = Field(...)

    @root_validator(pre=True)
    def validate_min_not_more_max(cls, values) -> Optional[int]:
        pass

    @validator('min_v')
    def validate_min_v(cls, value) -> Optional[int]:
        pass