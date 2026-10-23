

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_webhooks_id_response_webhook import PatchWebhooksIdResponseWebhook


class PatchWebhooksIdResponse(UniversalBaseModel):
    webhook: typing.Optional[PatchWebhooksIdResponseWebhook] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
