

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_attribute_set import RemoteAttributeSet
from .url import Url


class RemoteCallbackSubscribeCallbackWebhook(UniversalBaseModel):
    attributes: typing.Optional[RemoteAttributeSet] = None
    target: Url
    name: str = pydantic.Field()
    """
    Webhook name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
