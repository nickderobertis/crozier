

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .oauth_callback_url import OauthCallbackUrl


class OauthClientRead(UniversalBaseModel):
    callback_url: typing.Optional[typing.List[OauthCallbackUrl]] = pydantic.Field(default=None)
    """
    The callback URLs which are bound to this Oauth Client
    """

    client_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Client ID associated with this Oauth Client
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The display name of this Oauth Client
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Id of the client.
    """

    secret: typing.Optional[str] = pydantic.Field(default=None)
    """
    Secret associated with this Oauth Client
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the pack group, can be ACTIVE, CANCELLED or CANCELLED_PENDING.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
