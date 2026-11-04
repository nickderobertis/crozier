

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .value_event_operation import ValueEventOperation


class ValueEvent(UniversalBaseModel):
    bucket: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    revision: typing.Optional[int] = None
    delta: typing.Optional[int] = None
    operation: typing.Optional[ValueEventOperation] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
