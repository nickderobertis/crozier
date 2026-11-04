

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContributorOut(UniversalBaseModel):
    country: str
    created_at: dt.datetime
    id: int
    mosaic_url: typing.Optional[str] = None
    name: str
    screenshot_url: typing.Optional[str] = None
    series_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
