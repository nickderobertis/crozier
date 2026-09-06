

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_token_request_client_assertion_type import AccessTokenRequestClientAssertionType
from .access_token_request_grant_type import AccessTokenRequestGrantType


class AccessTokenRequest(UniversalBaseModel):
    assertion: typing.Optional[str] = pydantic.Field(default=None)
    """
    The assertion that is used to get a token, required with grant_type private_key_jwt
    """

    client_assertion_type: typing.Optional[AccessTokenRequestClientAssertionType] = pydantic.Field(default=None)
    """
    Required with grant_type private_key_jwt
    """

    client_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Required with grant_type private_key_jwt
    """

    grant_type: AccessTokenRequestGrantType = pydantic.Field()
    """
    The Grant Type
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
