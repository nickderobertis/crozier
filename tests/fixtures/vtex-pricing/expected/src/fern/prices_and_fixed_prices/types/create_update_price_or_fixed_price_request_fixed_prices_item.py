

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .create_update_price_or_fixed_price_request_fixed_prices_item_date_range import (
    CreateUpdatePriceOrFixedPriceRequestFixedPricesItemDateRange,
)


class CreateUpdatePriceOrFixedPriceRequestFixedPricesItem(UniversalBaseModel):
    """
    Array with general information about the SKU's fixed prices.
    """

    date_range: typing_extensions.Annotated[
        typing.Optional[CreateUpdatePriceOrFixedPriceRequestFixedPricesItemDateRange],
        FieldMetadata(alias="dateRange"),
        pydantic.Field(
            alias="dateRange", description="Period of time when the fixed price will be applied to the SKU."
        ),
    ] = None
    """
    Period of time when the fixed price will be applied to the SKU.
    """

    list_price: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="listPrice"),
        pydantic.Field(alias="listPrice", description="SKU List Fixed Price."),
    ] = None
    """
    SKU List Fixed Price.
    """

    min_quantity: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="minQuantity"),
        pydantic.Field(
            alias="minQuantity", description="Minimum quantity of the SKU for the fixed price to be applied."
        ),
    ]
    """
    Minimum quantity of the SKU for the fixed price to be applied.
    """

    trade_policy_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="tradePolicyId"),
        pydantic.Field(
            alias="tradePolicyId", description="Trade policy name or ID that will have the fixed price configured."
        ),
    ]
    """
    Trade policy name or ID that will have the fixed price configured.
    """

    value: float = pydantic.Field()
    """
    Fixed price value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
