

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .snssai import Snssai


class ConfiguredSnssai(UniversalBaseModel):
    configured_snssai: typing_extensions.Annotated[
        Snssai, FieldMetadata(alias="configuredSnssai"), pydantic.Field(alias="configuredSnssai")
    ]
    mapped_home_snssai: typing_extensions.Annotated[
        typing.Optional[Snssai], FieldMetadata(alias="mappedHomeSnssai"), pydantic.Field(alias="mappedHomeSnssai")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
