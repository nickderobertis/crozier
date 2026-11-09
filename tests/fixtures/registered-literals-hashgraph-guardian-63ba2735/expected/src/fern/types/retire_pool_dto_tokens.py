

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .retire_pool_dto_tokens_type import RetirePoolDtoTokensType


class RetirePoolDtoTokens(UniversalBaseModel):
    token: typing.Optional[str] = None
    contract: typing.Optional[str] = None
    count: typing.Optional[float] = None
    decimals: typing.Optional[float] = None
    type: typing.Optional[RetirePoolDtoTokensType] = None
    token_symbol: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tokenSymbol"), pydantic.Field(alias="tokenSymbol")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
