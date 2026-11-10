

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item import Item
from .request_id import RequestId


class ItemWebhookUpdateResponse(UniversalBaseModel):
    """
    ItemWebhookUpdateResponse defines the response schema for `/item/webhook/update`
    """

    item: Item
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
