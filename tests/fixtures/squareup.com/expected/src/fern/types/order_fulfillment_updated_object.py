

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .order_fulfillment_updated import OrderFulfillmentUpdated


class OrderFulfillmentUpdatedObject(UniversalBaseModel):
    """ """

    order_fulfillment_updated: typing.Optional[OrderFulfillmentUpdated] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
