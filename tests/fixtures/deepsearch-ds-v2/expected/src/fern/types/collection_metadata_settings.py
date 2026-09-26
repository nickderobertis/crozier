

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CollectionMetadataSettings(UniversalBaseModel):
    description: typing.Optional[str] = None
    display_name: typing.Optional[str] = None
    license: typing.Optional[str] = None
    source: typing.Optional[str] = None
    version: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
