

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ObtainTokenResponse(UniversalBaseModel):
    """ """

    access_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    A valid OAuth access token. OAuth access tokens are 64 bytes long.
    Provide the access token in a header with every request to Connect API
    endpoints. See [OAuth API: Walkthrough](https://developer.squareup.com/docs/oauth-api/walkthrough)
    for more information.
    """

    expires_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date when access_token expires, in [ISO 8601](http://www.iso.org/iso/home/standards/iso8601.htm) format.
    """

    id_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Then OpenID token belonging to this this person. Only present if the
    OPENID scope is included in the authorize request.
    """

    merchant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the authorizing merchant's business.
    """

    plan_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    __LEGACY FIELD__. The ID of the subscription plan the merchant signed
    up for. Only present if the merchant signed up for a subscription during
    authorization.
    """

    refresh_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    A refresh token. OAuth refresh tokens are 64 bytes long.
    For more information, see [OAuth access token management](https://developer.squareup.com/docs/oauth-api/how-it-works#oauth-access-token-management).
    """

    short_lived: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean indicating the access token is a short-lived access token.
    The short-lived access token returned in the response will expire in 24 hours.
    """

    subscription_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    __LEGACY FIELD__. The ID of a subscription plan the merchant signed up
    for. Only present if the merchant signed up for a subscription during authorization.
    """

    token_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    This value is always _bearer_.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
