

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .anchored import Anchored


class Holder(UniversalBaseModel):
    via_pointer: typing_extensions.Annotated[
        Anchored, FieldMetadata(alias="viaPointer"), pydantic.Field(alias="viaPointer")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
