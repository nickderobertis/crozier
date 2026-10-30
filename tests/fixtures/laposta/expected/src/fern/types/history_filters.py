

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class HistoryFilters(UniversalBaseModel):
    timezone: typing.Optional[str] = None
    campaign_id: typing.Optional[str] = None
    event_date_from: typing.Optional[str] = None
    event_date_from_iso: typing.Optional[str] = None
    event_date_to: typing.Optional[str] = None
    event_date_to_iso: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
