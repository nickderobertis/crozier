

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BasicBotBaseServicesItemBaseUrl(UniversalBaseModel):
    """
    When the bot is an outgoing webhook.
    """

    base_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL the outgoing webhook is configured to post to.
    """

    token: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique token that the third-party service can use to confirm
    that the request is indeed coming from Zulip.
    """

    interface: typing.Optional[int] = pydantic.Field(default=None)
    """
    An integer indicating what format requests are posted in:
    
    - 1 = Zulip's native outgoing webhook format.
    - 2 = Emulate the Slack outgoing webhook format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
