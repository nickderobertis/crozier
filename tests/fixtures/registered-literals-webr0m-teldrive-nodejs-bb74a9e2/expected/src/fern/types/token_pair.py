

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .token_pair_token_type import TokenPairTokenType


class TokenPair(UniversalBaseModel):
    access_token: typing_extensions.Annotated[
        str, FieldMetadata(alias="accessToken"), pydantic.Field(alias="accessToken")
    ]
    refresh_token: typing_extensions.Annotated[
        str, FieldMetadata(alias="refreshToken"), pydantic.Field(alias="refreshToken")
    ]
    token_type: typing_extensions.Annotated[
        TokenPairTokenType, FieldMetadata(alias="tokenType"), pydantic.Field(alias="tokenType")
    ]
    expires_in: typing_extensions.Annotated[int, FieldMetadata(alias="expiresIn"), pydantic.Field(alias="expiresIn")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
