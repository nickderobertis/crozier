

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_webhooks_response_data_item import GetWebhooksResponseDataItem
from .get_webhooks_response_meta import GetWebhooksResponseMeta


class GetWebhooksResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[GetWebhooksResponseDataItem]] = None
    meta: typing.Optional[GetWebhooksResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
