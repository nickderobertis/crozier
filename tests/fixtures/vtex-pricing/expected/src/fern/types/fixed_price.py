

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .date_range import DateRange


class FixedPrice(UniversalBaseModel):
    date_range: typing_extensions.Annotated[
        typing.Optional[DateRange], FieldMetadata(alias="dateRange"), pydantic.Field(alias="dateRange")
    ] = None
    list_price: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="listPrice"),
        pydantic.Field(alias="listPrice", description="Trade Policy List Price Value."),
    ] = None
    """
    Trade Policy List Price Value.
    """

    min_quantity: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="minQuantity"),
        pydantic.Field(alias="minQuantity", description="Trade Policy Fixed Price Minimum Item Quantity."),
    ]
    """
    Trade Policy Fixed Price Minimum Item Quantity.
    """

    trade_policy_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="tradePolicyId"), pydantic.Field(alias="tradePolicyId", description="Trade Policy ID.")
    ]
    """
    Trade Policy ID.
    """

    value: float = pydantic.Field()
    """
    Trade Policy Fixed Price Value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
