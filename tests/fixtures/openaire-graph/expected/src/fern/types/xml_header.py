

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class XmlHeader(UniversalBaseModel):
    query: typing.Optional[str] = None
    locale: typing.Optional[str] = None
    size: typing.Optional[int] = None
    page: typing.Optional[int] = None
    total: typing.Optional[int] = None
    fields: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
