

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Meta(UniversalBaseModel):
    found: typing.Optional[int] = None
    license: typing.Optional[str] = None
    limit: typing.Optional[int] = None
    name: typing.Optional[str] = None
    page: typing.Optional[int] = None
    website: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
