

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .kiln import Kiln


class LoadReservedKiln(Kiln):
    reserved_until: typing_extensions.Annotated[
        str, FieldMetadata(alias="reservedUntil"), pydantic.Field(alias="reservedUntil")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
