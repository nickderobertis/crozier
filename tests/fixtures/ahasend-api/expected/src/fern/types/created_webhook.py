

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .webhook import Webhook


class CreatedWebhook(Webhook):
    secret: str = pydantic.Field()
    """
    Webhook signing secret. Returned only when the webhook is created.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
