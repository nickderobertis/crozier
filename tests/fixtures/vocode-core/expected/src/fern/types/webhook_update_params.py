

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .webhook_update_params_method import WebhookUpdateParamsMethod
from .webhook_update_params_subscriptions import WebhookUpdateParamsSubscriptions
from .webhook_update_params_url import WebhookUpdateParamsUrl


class WebhookUpdateParams(UniversalBaseModel):
    subscriptions: typing.Optional[WebhookUpdateParamsSubscriptions] = None
    url: typing.Optional[WebhookUpdateParamsUrl] = None
    method: typing.Optional[WebhookUpdateParamsMethod] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
