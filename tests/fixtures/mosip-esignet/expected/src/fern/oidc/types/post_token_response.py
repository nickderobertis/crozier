

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_token_response_token_type import PostTokenResponseTokenType


class PostTokenResponse(UniversalBaseModel):
    id_token: str = pydantic.Field()
    """
    Identity token in JWT format. Will have the below claims in the payload.
    <ul>
    <li>iss</li>
    <li>sub - (PSUT)</li>
    <li>aud</li>
    <li>exp</li>
    <li>iat</li>
    <li>auth_time</li>
    <li>nonce</li>
    <li>acr</li>
    <li>at_hash</li>
    </ul>
    """

    access_token: str = pydantic.Field()
    """
    The access token in JWT format. This token that will be used to call the UserInfo endpoint.
    """

    token_type: PostTokenResponseTokenType = pydantic.Field()
    """
    The type of the access token, set to Bearer
    """

    expires_in: float = pydantic.Field()
    """
    The lifetime of the access token, in seconds.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
