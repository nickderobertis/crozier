

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .incoming_webhook_update_for_interaction_callback_request_partial import (
    IncomingWebhookUpdateForInteractionCallbackRequestPartial,
)


class UpdateMessageInteractionCallbackRequest(UniversalBaseModel):
    type: int
    data: typing.Optional[IncomingWebhookUpdateForInteractionCallbackRequestPartial] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
