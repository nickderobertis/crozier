

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TokenInfo(UniversalBaseModel):
    id: str
    token_id: typing_extensions.Annotated[str, FieldMetadata(alias="tokenId"), pydantic.Field(alias="tokenId")]
    token_name: typing_extensions.Annotated[str, FieldMetadata(alias="tokenName"), pydantic.Field(alias="tokenName")]
    token_symbol: typing_extensions.Annotated[
        str, FieldMetadata(alias="tokenSymbol"), pydantic.Field(alias="tokenSymbol")
    ]
    token_type: typing_extensions.Annotated[str, FieldMetadata(alias="tokenType"), pydantic.Field(alias="tokenType")]
    decimals: str
    associated: bool
    balance: str
    frozen: bool
    kyc: bool
    enable_admin: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="enableAdmin"), pydantic.Field(alias="enableAdmin")
    ] = None
    enable_kyc: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="enableKYC"), pydantic.Field(alias="enableKYC")
    ] = None
    enable_freeze: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="enableFreeze"), pydantic.Field(alias="enableFreeze")
    ] = None
    enable_wipe: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="enableWipe"), pydantic.Field(alias="enableWipe")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
