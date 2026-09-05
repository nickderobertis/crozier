

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Getcomputedprice(UniversalBaseModel):
    cost_price: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="costPrice"),
        pydantic.Field(alias="costPrice", description="Cost price."),
    ] = None
    """
    Cost price.
    """

    list_price: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="listPrice"),
        pydantic.Field(alias="listPrice", description='Trade Policy List Price, also known as "from" price.'),
    ]
    """
    Trade Policy List Price, also known as "from" price.
    """

    price_valid_until: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="priceValidUntil"),
        pydantic.Field(
            alias="priceValidUntil",
            description="Date until when the computed price will be valid, due to price scheduling. If no price scheduling applies, this will be set a year from the current time.",
        ),
    ]
    """
    Date until when the computed price will be valid, due to price scheduling. If no price scheduling applies, this will be set a year from the current time.
    """

    selling_price: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="sellingPrice"),
        pydantic.Field(
            alias="sellingPrice",
            description="Computed Price before applying coupons, promotions and taxes. This price may change before reaching the shelf.",
        ),
    ]
    """
    Computed Price before applying coupons, promotions and taxes. This price may change before reaching the shelf.
    """

    trade_policy_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="tradePolicyId"), pydantic.Field(alias="tradePolicyId", description="Trade Policy ID.")
    ]
    """
    Trade Policy ID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
