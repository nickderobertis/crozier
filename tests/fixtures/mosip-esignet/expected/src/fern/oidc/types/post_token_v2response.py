

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_token_v2response_token_type import PostTokenV2ResponseTokenType


class PostTokenV2Response(UniversalBaseModel):
    id_token: typing.Optional[str] = pydantic.Field(default=None)
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
    
    It is non-null only in OIDC flow. otherwise the id_token is not returned.
    """

    access_token: str = pydantic.Field()
    """
    The access token in JWT format. This token that will be used to call the UserInfo endpoint.
    """

    token_type: PostTokenV2ResponseTokenType = pydantic.Field()
    """
    The type of the access token, set to either Bearer or DPoP
    """

    expires_in: float = pydantic.Field()
    """
    The lifetime of the access token, in seconds.
    """

    c_nonce: typing.Optional[str] = pydantic.Field(default=None)
    """
    JSON string containing a nonce to be used to create a proof of possession of key material when requesting a Credential.
    """

    c_nonce_expires_in: typing.Optional[float] = pydantic.Field(default=None)
    """
    JSON integer denoting the lifetime in seconds of the c_nonce.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
