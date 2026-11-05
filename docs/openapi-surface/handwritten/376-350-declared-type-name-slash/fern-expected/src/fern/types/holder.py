

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .gad_get import GadGet
from .thing import Thing


class Holder(UniversalBaseModel):
    widget: typing.Optional[GadGet] = None
    widgets: typing.Optional[typing.List[GadGet]] = None
    thing: typing.Optional[Thing] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
