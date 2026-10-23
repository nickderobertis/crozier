

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_webhooks_response_webhook import PostWebhooksResponseWebhook


class PostWebhooksResponse(UniversalBaseModel):
    webhook: typing.Optional[PostWebhooksResponseWebhook] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
