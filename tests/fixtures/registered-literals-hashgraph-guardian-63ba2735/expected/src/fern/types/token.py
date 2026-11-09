

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Token(UniversalBaseModel):
    change_supply: typing_extensions.Annotated[
        bool, FieldMetadata(alias="changeSupply"), pydantic.Field(alias="changeSupply")
    ]
    decimals: str
    enable_admin: typing_extensions.Annotated[
        bool, FieldMetadata(alias="enableAdmin"), pydantic.Field(alias="enableAdmin")
    ]
    enable_freeze: typing_extensions.Annotated[
        bool, FieldMetadata(alias="enableFreeze"), pydantic.Field(alias="enableFreeze")
    ]
    enable_kyc: typing_extensions.Annotated[bool, FieldMetadata(alias="enableKYC"), pydantic.Field(alias="enableKYC")]
    enable_wipe: typing_extensions.Annotated[
        bool, FieldMetadata(alias="enableWipe"), pydantic.Field(alias="enableWipe")
    ]
    initial_supply: typing_extensions.Annotated[
        str, FieldMetadata(alias="initialSupply"), pydantic.Field(alias="initialSupply")
    ]
    token_name: typing_extensions.Annotated[str, FieldMetadata(alias="tokenName"), pydantic.Field(alias="tokenName")]
    token_symbol: typing_extensions.Annotated[
        str, FieldMetadata(alias="tokenSymbol"), pydantic.Field(alias="tokenSymbol")
    ]
    token_type: typing_extensions.Annotated[str, FieldMetadata(alias="tokenType"), pydantic.Field(alias="tokenType")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
