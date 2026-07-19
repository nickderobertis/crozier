

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .client_side_access_tokens_create_client_side_access_token_response_policy import (
    ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicy,
)


class ClientSideAccessTokensCreateClientSideAccessTokenResponse(UniversalBaseModel):
    policy: ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicy
    token: str
    hostname: str
    expires_at: typing_extensions.Annotated[str, FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
