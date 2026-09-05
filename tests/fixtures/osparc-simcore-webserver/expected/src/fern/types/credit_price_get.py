

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CreditPriceGet(UniversalBaseModel):
    product_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="productName"), pydantic.Field(alias="productName")
    ]
    usd_per_credit: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="usdPerCredit"),
        pydantic.Field(
            alias="usdPerCredit",
            description="Price of a credit in USD. If None, then this product's price is UNDEFINED",
        ),
    ] = None
    """
    Price of a credit in USD. If None, then this product's price is UNDEFINED
    """

    min_payment_amount_usd: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="minPaymentAmountUsd"),
        pydantic.Field(
            alias="minPaymentAmountUsd",
            description="Minimum amount (included) in USD that can be paid for this productCan be None if this product's price is UNDEFINED",
        ),
    ] = None
    """
    Minimum amount (included) in USD that can be paid for this productCan be None if this product's price is UNDEFINED
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
