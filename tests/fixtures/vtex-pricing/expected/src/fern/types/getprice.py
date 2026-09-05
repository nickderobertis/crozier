

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .fixed_price import FixedPrice


class Getprice(UniversalBaseModel):
    base_price: typing_extensions.Annotated[
        int, FieldMetadata(alias="basePrice"), pydantic.Field(alias="basePrice", description="SKU's reference price.")
    ]
    """
    SKU's reference price.
    """

    cost_price: typing_extensions.Annotated[
        int, FieldMetadata(alias="costPrice"), pydantic.Field(alias="costPrice", description="SKU's cost price.")
    ]
    """
    SKU's cost price.
    """

    fixed_prices: typing_extensions.Annotated[
        typing.List[FixedPrice],
        FieldMetadata(alias="fixedPrices"),
        pydantic.Field(
            alias="fixedPrices",
            description="The fixed price is a price that overlaps all other existing price configurations of a price table.",
        ),
    ]
    """
    The fixed price is a price that overlaps all other existing price configurations of a price table.
    """

    item_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="itemId"), pydantic.Field(alias="itemId", description="SKU ID.")
    ]
    """
    SKU ID.
    """

    list_price: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="listPrice"),
        pydantic.Field(alias="listPrice", description="Suggested retail price for the SKU."),
    ]
    """
    Suggested retail price for the SKU.
    """

    markup: int = pydantic.Field()
    """
    Desired profit margin with the SKU's sale.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
