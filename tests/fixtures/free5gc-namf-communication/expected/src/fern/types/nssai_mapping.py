

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .snssai import Snssai


class NssaiMapping(UniversalBaseModel):
    mapped_snssai: typing_extensions.Annotated[
        Snssai, FieldMetadata(alias="mappedSnssai"), pydantic.Field(alias="mappedSnssai")
    ]
    h_snssai: typing_extensions.Annotated[Snssai, FieldMetadata(alias="hSnssai"), pydantic.Field(alias="hSnssai")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
