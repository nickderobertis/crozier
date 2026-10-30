

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class HistoryDataItemEvent(UniversalBaseModel):
    type: typing.Optional[str] = None
    timezone: typing.Optional[str] = None
    event_date: typing.Optional[str] = None
    event_date_iso: typing.Optional[str] = None
    campaign: typing.Optional[typing.Dict[str, typing.Any]] = None
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
