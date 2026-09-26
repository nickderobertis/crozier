

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_callback_subscribe_callback_webhook import RemoteCallbackSubscribeCallbackWebhook


class RemoteCallbackSubscribeCallback(UniversalBaseModel):
    webhook: RemoteCallbackSubscribeCallbackWebhook

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
