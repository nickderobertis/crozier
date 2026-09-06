

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .ecomm_order_changed_payload_payload_all_addresses_item import EcommOrderChangedPayloadPayloadAllAddressesItem
from .ecomm_order_changed_payload_payload_application_fee import EcommOrderChangedPayloadPayloadApplicationFee
from .ecomm_order_changed_payload_payload_billing_address import EcommOrderChangedPayloadPayloadBillingAddress
from .ecomm_order_changed_payload_payload_customer_info import EcommOrderChangedPayloadPayloadCustomerInfo
from .ecomm_order_changed_payload_payload_customer_paid import EcommOrderChangedPayloadPayloadCustomerPaid
from .ecomm_order_changed_payload_payload_dispute_last_status import EcommOrderChangedPayloadPayloadDisputeLastStatus
from .ecomm_order_changed_payload_payload_download_files_item import EcommOrderChangedPayloadPayloadDownloadFilesItem
from .ecomm_order_changed_payload_payload_metadata import EcommOrderChangedPayloadPayloadMetadata
from .ecomm_order_changed_payload_payload_net_amount import EcommOrderChangedPayloadPayloadNetAmount
from .ecomm_order_changed_payload_payload_paypal_details import EcommOrderChangedPayloadPayloadPaypalDetails
from .ecomm_order_changed_payload_payload_purchased_items_item import EcommOrderChangedPayloadPayloadPurchasedItemsItem
from .ecomm_order_changed_payload_payload_shipping_address import EcommOrderChangedPayloadPayloadShippingAddress
from .ecomm_order_changed_payload_payload_status import EcommOrderChangedPayloadPayloadStatus
from .ecomm_order_changed_payload_payload_stripe_card import EcommOrderChangedPayloadPayloadStripeCard
from .ecomm_order_changed_payload_payload_stripe_details import EcommOrderChangedPayloadPayloadStripeDetails
from .ecomm_order_changed_payload_payload_totals import EcommOrderChangedPayloadPayloadTotals


class EcommOrderChangedPayloadPayload(UniversalBaseModel):
    order_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="orderId"),
        pydantic.Field(
            alias="orderId",
            description="The order ID. Will usually be 6 hex characters, but can also be 9\nhex characters if the site has a very large number of Orders.\nRandomly assigned.",
        ),
    ] = None
    """
    The order ID. Will usually be 6 hex characters, but can also be 9
    hex characters if the site has a very large number of Orders.
    Randomly assigned.
    """

    status: typing.Optional[EcommOrderChangedPayloadPayloadStatus] = pydantic.Field(default=None)
    """
    The status of the Order
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    A comment string for this Order, which is editable by API user (not used by Webflow).
    """

    order_comment: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="orderComment"),
        pydantic.Field(alias="orderComment", description="A comment that the customer left when making their Order"),
    ] = None
    """
    A comment that the customer left when making their Order
    """

    accepted_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="acceptedOn"),
        pydantic.Field(alias="acceptedOn", description="The ISO8601 timestamp that an Order was placed."),
    ] = None
    """
    The ISO8601 timestamp that an Order was placed.
    """

    fulfilled_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="fulfilledOn"),
        pydantic.Field(
            alias="fulfilledOn",
            description="When an Order is marked as 'fulfilled', this field represents the timestamp of the fulfillment in ISO8601 format. Otherwise, it is null.",
        ),
    ] = None
    """
    When an Order is marked as 'fulfilled', this field represents the timestamp of the fulfillment in ISO8601 format. Otherwise, it is null.
    """

    refunded_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="refundedOn"),
        pydantic.Field(
            alias="refundedOn",
            description="When an Order is marked as 'refunded', this field represents the timestamp of the fulfillment in ISO8601 format. Otherwise, it is null.",
        ),
    ] = None
    """
    When an Order is marked as 'refunded', this field represents the timestamp of the fulfillment in ISO8601 format. Otherwise, it is null.
    """

    disputed_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="disputedOn"),
        pydantic.Field(
            alias="disputedOn",
            description="When an Order is marked as 'disputed', this field represents the timestamp of the fulfillment in ISO8601 format. Otherwise, it is null.",
        ),
    ] = None
    """
    When an Order is marked as 'disputed', this field represents the timestamp of the fulfillment in ISO8601 format. Otherwise, it is null.
    """

    dispute_updated_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="disputeUpdatedOn"),
        pydantic.Field(
            alias="disputeUpdatedOn",
            description="If an Order has been disputed by the customer, this key will be set to the ISO8601 timestamp of the last update received. If the Order is not disputed, the key will be null.",
        ),
    ] = None
    """
    If an Order has been disputed by the customer, this key will be set to the ISO8601 timestamp of the last update received. If the Order is not disputed, the key will be null.
    """

    dispute_last_status: typing_extensions.Annotated[
        typing.Optional[EcommOrderChangedPayloadPayloadDisputeLastStatus],
        FieldMetadata(alias="disputeLastStatus"),
        pydantic.Field(
            alias="disputeLastStatus",
            description="If an order was disputed by the customer, then this key will be set with the [dispute's status](https://stripe.com/docs/api#dispute_object-status).",
        ),
    ] = None
    """
    If an order was disputed by the customer, then this key will be set with the [dispute's status](https://stripe.com/docs/api#dispute_object-status).
    """

    customer_paid: typing_extensions.Annotated[
        typing.Optional[EcommOrderChangedPayloadPayloadCustomerPaid],
        FieldMetadata(alias="customerPaid"),
        pydantic.Field(alias="customerPaid", description="The total paid by the customer"),
    ] = None
    """
    The total paid by the customer
    """

    net_amount: typing_extensions.Annotated[
        typing.Optional[EcommOrderChangedPayloadPayloadNetAmount],
        FieldMetadata(alias="netAmount"),
        pydantic.Field(alias="netAmount", description="The net amount after application fees"),
    ] = None
    """
    The net amount after application fees
    """

    application_fee: typing_extensions.Annotated[
        typing.Optional[EcommOrderChangedPayloadPayloadApplicationFee],
        FieldMetadata(alias="applicationFee"),
        pydantic.Field(alias="applicationFee", description="The application fee assessed by the platform"),
    ] = None
    """
    The application fee assessed by the platform
    """

    all_addresses: typing_extensions.Annotated[
        typing.Optional[typing.List[EcommOrderChangedPayloadPayloadAllAddressesItem]],
        FieldMetadata(alias="allAddresses"),
        pydantic.Field(
            alias="allAddresses", description="All addresses provided by the customer during the ordering flow."
        ),
    ] = None
    """
    All addresses provided by the customer during the ordering flow.
    """

    shipping_address: typing_extensions.Annotated[
        typing.Optional[EcommOrderChangedPayloadPayloadShippingAddress],
        FieldMetadata(alias="shippingAddress"),
        pydantic.Field(alias="shippingAddress", description="The shipping address"),
    ] = None
    """
    The shipping address
    """

    billing_address: typing_extensions.Annotated[
        typing.Optional[EcommOrderChangedPayloadPayloadBillingAddress],
        FieldMetadata(alias="billingAddress"),
        pydantic.Field(alias="billingAddress", description="The billing address"),
    ] = None
    """
    The billing address
    """

    shipping_provider: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="shippingProvider"),
        pydantic.Field(
            alias="shippingProvider",
            description="A string editable by the API user to note the shipping provider used (not used by Webflow).",
        ),
    ] = None
    """
    A string editable by the API user to note the shipping provider used (not used by Webflow).
    """

    shipping_tracking: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="shippingTracking"),
        pydantic.Field(
            alias="shippingTracking",
            description="A string editable by the API user to note the shipping tracking number for the order (not used by Webflow).",
        ),
    ] = None
    """
    A string editable by the API user to note the shipping tracking number for the order (not used by Webflow).
    """

    shipping_tracking_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="shippingTrackingURL"), pydantic.Field(alias="shippingTrackingURL")
    ] = None
    customer_info: typing_extensions.Annotated[
        typing.Optional[EcommOrderChangedPayloadPayloadCustomerInfo],
        FieldMetadata(alias="customerInfo"),
        pydantic.Field(alias="customerInfo", description="An object with the keys `fullName` and `email`."),
    ] = None
    """
    An object with the keys `fullName` and `email`.
    """

    purchased_items: typing_extensions.Annotated[
        typing.Optional[typing.List[EcommOrderChangedPayloadPayloadPurchasedItemsItem]],
        FieldMetadata(alias="purchasedItems"),
        pydantic.Field(alias="purchasedItems", description="An array of all things that the Customer purchased."),
    ] = None
    """
    An array of all things that the Customer purchased.
    """

    purchased_items_count: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="purchasedItemsCount"),
        pydantic.Field(alias="purchasedItemsCount", description="The sum of all 'count' fields in 'purchasedItems'."),
    ] = None
    """
    The sum of all 'count' fields in 'purchasedItems'.
    """

    stripe_details: typing_extensions.Annotated[
        typing.Optional[EcommOrderChangedPayloadPayloadStripeDetails],
        FieldMetadata(alias="stripeDetails"),
        pydantic.Field(
            alias="stripeDetails",
            description="An object with various Stripe IDs, useful for linking into the stripe dashboard.",
        ),
    ] = None
    """
    An object with various Stripe IDs, useful for linking into the stripe dashboard.
    """

    stripe_card: typing_extensions.Annotated[
        typing.Optional[EcommOrderChangedPayloadPayloadStripeCard],
        FieldMetadata(alias="stripeCard"),
        pydantic.Field(
            alias="stripeCard",
            description="Details on the card used to fulfill this order, if this order was finalized with Stripe.",
        ),
    ] = None
    """
    Details on the card used to fulfill this order, if this order was finalized with Stripe.
    """

    paypal_details: typing_extensions.Annotated[
        typing.Optional[EcommOrderChangedPayloadPayloadPaypalDetails],
        FieldMetadata(alias="paypalDetails"),
        pydantic.Field(alias="paypalDetails"),
    ] = None
    custom_data: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="customData"),
        pydantic.Field(
            alias="customData",
            description="An array of additional inputs for custom order data gathering. Each object in the array represents an input with a name, and a textInput, textArea, or checkbox value.",
        ),
    ] = None
    """
    An array of additional inputs for custom order data gathering. Each object in the array represents an input with a name, and a textInput, textArea, or checkbox value.
    """

    metadata: typing.Optional[EcommOrderChangedPayloadPayloadMetadata] = None
    is_customer_deleted: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isCustomerDeleted"),
        pydantic.Field(
            alias="isCustomerDeleted",
            description="A boolean indicating whether the customer has been deleted from the site.",
        ),
    ] = None
    """
    A boolean indicating whether the customer has been deleted from the site.
    """

    is_shipping_required: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isShippingRequired"),
        pydantic.Field(
            alias="isShippingRequired",
            description="A boolean indicating whether the order contains one or more purchased items that require shipping.",
        ),
    ] = None
    """
    A boolean indicating whether the order contains one or more purchased items that require shipping.
    """

    has_downloads: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasDownloads"),
        pydantic.Field(
            alias="hasDownloads",
            description="A boolean indicating whether the order contains one or more purchased items that are downloadable.",
        ),
    ] = None
    """
    A boolean indicating whether the order contains one or more purchased items that are downloadable.
    """

    payment_processor: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="paymentProcessor"),
        pydantic.Field(
            alias="paymentProcessor", description="A string indicating the payment processor used for this order."
        ),
    ] = None
    """
    A string indicating the payment processor used for this order.
    """

    totals: typing.Optional[EcommOrderChangedPayloadPayloadTotals] = pydantic.Field(default=None)
    """
    An object describing various pricing totals
    """

    download_files: typing_extensions.Annotated[
        typing.Optional[typing.List[EcommOrderChangedPayloadPayloadDownloadFilesItem]],
        FieldMetadata(alias="downloadFiles"),
        pydantic.Field(alias="downloadFiles", description="An array of downloadable file objects."),
    ] = None
    """
    An array of downloadable file objects.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
