

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OrderFulfillmentUpdatedUpdate(UniversalBaseModel):
    """
    Information about fulfillment updates.
    """

    fulfillment_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID that identifies the fulfillment only within this order.
    """

    new_state: typing.Optional[str] = pydantic.Field(default=None)
    """
    The state of the fulfillment after the change. The state might be equal to `old_state` if a non-state
    field was changed on the fulfillment (such as the tracking number).
    """

    old_state: typing.Optional[str] = pydantic.Field(default=None)
    """
    The state of the fulfillment before the change.
    The state is not populated if the fulfillment is created with this new `Order` version.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
