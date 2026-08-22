

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_response_account import AccountResponseAccount
from .bytes import Bytes
from .storage_proof import StorageProof


class AccountResponse(UniversalBaseModel):
    account: typing.Optional[AccountResponseAccount] = None
    code: typing.Optional[Bytes] = None
    account_proof: typing_extensions.Annotated[
        typing.Optional[typing.List[Bytes]], FieldMetadata(alias="accountProof"), pydantic.Field(alias="accountProof")
    ] = None
    storage_proof: typing_extensions.Annotated[
        typing.Optional[typing.List[StorageProof]],
        FieldMetadata(alias="storageProof"),
        pydantic.Field(alias="storageProof"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
