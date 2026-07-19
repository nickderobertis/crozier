

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .uuid_ import Uuid
from .webhook import Webhook


class WebhookWithId(Webhook):
    """
    Details of an existing registered webhook
    """

    id: Uuid = pydantic.Field()
    """
    Webhook identifier
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
