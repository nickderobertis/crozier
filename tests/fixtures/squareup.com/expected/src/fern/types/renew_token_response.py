

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RenewTokenResponse(UniversalBaseModel):
    """ """

    access_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    The renewed access token.
    This value might be different from the `access_token` you provided in your request.
    You provide this token in a header with every request to Connect API endpoints.
    See [Request and response headers](https://developer.squareup.com/docs/api/connect/v2/#requestandresponseheaders) for the format of this header.
    """

    expires_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date when access_token expires, in [ISO 8601](http://www.iso.org/iso/home/standards/iso8601.htm) format.
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

    subscription_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    __LEGACY FIELD__. The ID of the merchant subscription associated with
    the authorization. Only present if the merchant signed up for a subscription
    during authorization..
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
