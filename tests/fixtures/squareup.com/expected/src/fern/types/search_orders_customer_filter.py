

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SearchOrdersCustomerFilter(UniversalBaseModel):
    """
    A filter based on the order `customer_id` and any tender `customer_id`
    associated with the order. It does not filter based on the
    [FulfillmentRecipient](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderFulfillmentRecipient) `customer_id`.
    """

    customer_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of customer IDs to filter by.
    
    Max: 10 customer IDs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
