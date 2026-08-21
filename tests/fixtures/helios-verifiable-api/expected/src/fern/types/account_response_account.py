

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .hash32 import Hash32
from .uint64 import Uint64
from .uint256 import Uint256


class AccountResponseAccount(UniversalBaseModel):
    address: typing.Optional[Address] = None
    balance: typing.Optional[Uint256] = None
    nonce: typing.Optional[Uint64] = None
    code_hash: typing_extensions.Annotated[
        typing.Optional[Hash32], FieldMetadata(alias="codeHash"), pydantic.Field(alias="codeHash")
    ] = None
    storage_hash: typing_extensions.Annotated[
        typing.Optional[Hash32], FieldMetadata(alias="storageHash"), pydantic.Field(alias="storageHash")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
