

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_webhooks_response_webhooks_item import GetWebhooksResponseWebhooksItem


class GetWebhooksResponse(UniversalBaseModel):
    webhooks: typing.Optional[typing.List[GetWebhooksResponseWebhooksItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
