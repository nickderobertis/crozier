

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class XmlMeasure(UniversalBaseModel):
    id: typing.Optional[str] = None
    score: typing.Optional[str] = None
    clazz: typing.Optional[str] = None
    count: typing.Optional[str] = None
    datasource: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
