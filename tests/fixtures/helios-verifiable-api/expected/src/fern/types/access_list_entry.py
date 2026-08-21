

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .hash32 import Hash32


class AccessListEntry(UniversalBaseModel):
    address: Address
    storage_keys: typing_extensions.Annotated[
        typing.List[Hash32], FieldMetadata(alias="storageKeys"), pydantic.Field(alias="storageKeys")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
