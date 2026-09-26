

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tax_cloud_refund_tax import TaxCloudRefundTax


class TaxCloudRefundItemResponse(UniversalBaseModel):
    index: int = pydantic.Field()
    """
    Zero-based position of the item within the refund.
    """

    item_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="itemId"),
        pydantic.Field(
            alias="itemId", description="The itemId of the refunded line item, matching the original order."
        ),
    ]
    """
    The itemId of the refunded line item, matching the original order.
    """

    price: float = pydantic.Field()
    """
    The unit price refunded, calculated automatically from the order. When the order had discounts, this reflects the discounted amount actually paid.
    """

    quantity: float = pydantic.Field()
    """
    The quantity refunded.
    """

    tax: typing.Optional[TaxCloudRefundTax] = pydantic.Field(default=None)
    """
    The tax amount refunded for this line item.
    """

    tic: typing.Optional[int] = pydantic.Field(default=None)
    """
    Taxability Information Code (TIC) of the refunded item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
