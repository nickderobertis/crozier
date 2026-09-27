

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TelegramOwnerLinkResponse(UniversalBaseModel):
    start_url: str = pydantic.Field()
    """
    A one-time Telegram deep link the business admin opens or forwards to the owner. Tapping it delivers "/start <token>" to the bot; the first authentic tapper within the TTL becomes the verified owner. Single-use.
    """

    expires_in_seconds: int = pydantic.Field()
    """
    Seconds until the deep link expires.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
