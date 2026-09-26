

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ElasticMetadata(UniversalBaseModel):
    aliases: typing.Optional[typing.List[str]] = None
    created: typing.Optional[str] = None
    description: typing.Optional[str] = None
    display_name: typing.Optional[str] = None
    source: typing.Optional[str] = None
    storage: typing.Optional[str] = None
    version: typing.Optional[str] = None
    type: typing.Optional[str] = None
    domain: typing.Optional[typing.List[str]] = None
    classification: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
