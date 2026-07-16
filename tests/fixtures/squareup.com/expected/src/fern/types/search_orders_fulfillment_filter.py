

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SearchOrdersFulfillmentFilter(UniversalBaseModel):
    """
    Filter based on [order fulfillment](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderFulfillment) information.
    """

    fulfillment_states: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of [fulfillment states](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderFulfillmentState) to filter
    for. The list returns orders if any of its fulfillments match any of the
    fulfillment states listed in this field.
    """

    fulfillment_types: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of [fulfillment types](https://developer.squareup.com/reference/square_2021-08-18/enums/OrderFulfillmentType) to filter
    for. The list returns orders if any of its fulfillments match any of the fulfillment types
    listed in this field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
