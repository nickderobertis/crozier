

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .thing import Thing
from .widget import Widget


class Holder(UniversalBaseModel):
    widget: typing.Optional[Widget] = None
    widgets: typing.Optional[typing.List[Widget]] = None
    thing: typing.Optional[Thing] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
