

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PositionOrganization(UniversalBaseModel):
    industry: typing.Optional[str] = None
    name: typing.Optional[str] = None
    size: typing.Optional[str] = None
    ticker: typing.Optional[str] = None
    type: typing.Optional[str] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
