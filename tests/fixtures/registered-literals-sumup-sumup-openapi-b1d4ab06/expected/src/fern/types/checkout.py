

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .checkout_status import CheckoutStatus
from .checkout_transactions_item import CheckoutTransactionsItem
from .currency import Currency
from .mandate_response import MandateResponse


class Checkout(UniversalBaseModel):
    """
    Core checkout resource returned by the Checkouts API. A checkout is created before payment processing and then updated as payment attempts, redirects, and resulting transactions are attached to it.
    """

    checkout_reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    Merchant-defined reference for the checkout. Use it to correlate the SumUp checkout with your own order, cart, subscription, or payment attempt in your systems.
    """

    amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount to be charged to the payer, expressed in major units.
    """

    currency: typing.Optional[Currency] = None
    merchant_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Short unique identifier for the merchant that receives the payment.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Short merchant-defined description shown in SumUp tools and reporting. Use it to make the checkout easier to recognize in dashboards, support workflows, and reconciliation.
    """

    return_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional backend callback URL used by SumUp to notify your platform about processing updates for the checkout.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique SumUp identifier of the checkout resource.
    """

    status: typing.Optional[CheckoutStatus] = pydantic.Field(default=None)
    """
    Current high-level state of the checkout. `PENDING` means the checkout exists but is not yet completed, `PAID` means a payment succeeded, `FAILED` means the latest processing attempt failed, and `EXPIRED` means the checkout can no longer be processed.
    """

    date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp of when the checkout was created.
    """

    valid_until: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Optional expiration timestamp. The checkout must be processed before this moment, otherwise it becomes unusable. If omitted, the checkout does not have an explicit expiry time.
    """

    customer_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Merchant-scoped identifier of the customer associated with the checkout. Use it when storing payment instruments or reusing saved customer context for recurring and returning-payer flows.
    """

    mandate: typing.Optional[MandateResponse] = None
    hosted_checkout_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the SumUp-hosted payment page that handles the payment flow. Returned when Hosted Checkout is enabled for the checkout.
    """

    transactions: typing.Optional[typing.List[CheckoutTransactionsItem]] = pydantic.Field(default=None)
    """
    Payment attempts and resulting transaction records linked to this checkout. Use the Transactions endpoints when you need the authoritative payment result and event history.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
