

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tax_cloud_address import TaxCloudAddress
from .tax_cloud_cart_item_with_tax_response import TaxCloudCartItemWithTaxResponse
from .tax_cloud_currency import TaxCloudCurrency
from .tax_cloud_exemption import TaxCloudExemption
from .tax_cloud_order_response_kind import TaxCloudOrderResponseKind
from .tax_cloud_refund_response import TaxCloudRefundResponse


class TaxCloudOrderResponse(UniversalBaseModel):
    batch_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="batchId"),
        pydantic.Field(
            alias="batchId", description="Batch ID grouping this order with related orders, if one was supplied."
        ),
    ] = None
    """
    Batch ID grouping this order with related orders, if one was supplied.
    """

    channel: str = pydantic.Field()
    """
    The sales channel the order came from (e.g. amazon, ebay, walmart). Null when no channel was recorded.
    """

    completed_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="completedDate"),
        pydantic.Field(
            alias="completedDate",
            description="RFC3339 datetime the order was shipped/completed on, creating the tax liability. Absent for orders that are not yet completed.",
        ),
    ] = None
    """
    RFC3339 datetime the order was shipped/completed on, creating the tax liability. Absent for orders that are not yet completed.
    """

    connection_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="connectionId"),
        pydantic.Field(alias="connectionId", description="The TaxCloud connection the order was recorded under."),
    ]
    """
    The TaxCloud connection the order was recorded under.
    """

    currency: TaxCloudCurrency = pydantic.Field()
    """
    The currency the prices and tax amounts are denominated in.
    """

    customer_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="customerId"),
        pydantic.Field(alias="customerId", description="Your identifier for the customer in your own system."),
    ]
    """
    Your identifier for the customer in your own system.
    """

    delivered_by_seller: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="deliveredBySeller"),
        pydantic.Field(alias="deliveredBySeller", description="Whether the seller delivered the order directly."),
    ]
    """
    Whether the seller delivered the order directly.
    """

    destination: TaxCloudAddress = pydantic.Field()
    """
    The ship-to (destination) address of the order.
    """

    exclude_from_filing: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="excludeFromFiling"),
        pydantic.Field(alias="excludeFromFiling", description="Whether the order is excluded from tax filing."),
    ]
    """
    Whether the order is excluded from tax filing.
    """

    exemption: TaxCloudExemption = pydantic.Field()
    """
    The exemption information recorded on the order.
    """

    kind: TaxCloudOrderResponseKind = pydantic.Field()
    """
    The kind of order: 'order' for a sale or 'credit' for a credit order.
    """

    line_items: typing_extensions.Annotated[
        typing.Optional[typing.List[TaxCloudCartItemWithTaxResponse]],
        FieldMetadata(alias="lineItems"),
        pydantic.Field(alias="lineItems", description="The order's line items, each with its tax rate and amount."),
    ] = None
    """
    The order's line items, each with its tax rate and amount.
    """

    order_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="orderId"),
        pydantic.Field(alias="orderId", description="Your identifier for the order in your own system."),
    ]
    """
    Your identifier for the order in your own system.
    """

    origin: TaxCloudAddress = pydantic.Field()
    """
    The ship-from (origin) address of the order.
    """

    refunds: typing.Optional[typing.List[TaxCloudRefundResponse]] = pydantic.Field(default=None)
    """
    Refunds recorded against this order. Only included when the request set expand to 'refunds'.
    """

    transaction_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="transactionDate"),
        pydantic.Field(alias="transactionDate", description="RFC3339 datetime the order was purchased on."),
    ] = None
    """
    RFC3339 datetime the order was purchased on.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
