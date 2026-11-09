

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class SandboxItemFireWebhookResponse(UniversalBaseModel):
    """
    SandboxItemFireWebhookResponse defines the response schema for `/sandbox/item/fire_webhook`
    """

    request_id: RequestId
    webhook_fired: bool = pydantic.Field()
    """
    Value is `true`  if the test` webhook_code`  was successfully fired.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
