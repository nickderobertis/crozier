

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class Subscription(UniversalBaseModel):
    """
    Represents a customer subscription to a subscription plan.
    For an overview of the `Subscription` type, see
    [Subscription object](https://developer.squareup.com/docs/subscriptions-api/overview#subscription-object-overview).
    """

    canceled_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subscription cancellation date, in YYYY-MM-DD format (for
    example, 2013-01-15). On this date, the subscription status changes
    to `CANCELED` and the subscription billing stops.
    If you don't set this field, the subscription plan dictates if and
    when subscription ends.
    
    You cannot update this field, you can only clear it.
    """

    card_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the [customer](https://developer.squareup.com/reference/square_2021-08-18/objects/Customer) [card](https://developer.squareup.com/reference/square_2021-08-18/objects/Card)
    that is charged for the subscription.
    """

    charged_through_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date up to which the customer is invoiced for the
    subscription, in YYYY-MM-DD format (for example, 2013-01-15).
    
    After the invoice is sent for a given billing period,
    this date will be the last day of the billing period.
    For example,
    suppose for the month of May a customer gets an invoice
    (or charged the card) on May 1. For the monthly billing scenario,
    this date is then set to May 31.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the subscription was created, in RFC 3339 format.
    """

    customer_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the associated [customer](https://developer.squareup.com/reference/square_2021-08-18/objects/Customer) profile.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-assigned ID of the subscription.
    """

    invoice_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The IDs of the [invoices](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) created for the
    subscription, listed in order when the invoices were created
    (oldest invoices appear first).
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the location associated with the subscription.
    """

    plan_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the associated [subscription plan](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogSubscriptionPlan).
    """

    price_override_money: typing.Optional[Money] = None
    start_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The start date of the subscription, in YYYY-MM-DD format (for example,
    2013-01-15).
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The current status of the subscription.
    """

    tax_percentage: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tax amount applied when billing the subscription. The
    percentage is expressed in decimal form, using a `'.'` as the decimal
    separator and without a `'%'` sign. For example, a value of `7.5`
    corresponds to 7.5%.
    """

    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    Timezone that will be used in date calculations for the subscription.
    Defaults to the timezone of the location based on `location_id`.
    Format: the IANA Timezone Database identifier for the location timezone (for example, `America/Los_Angeles`).
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version of the object. When updating an object, the version
    supplied must match the version in the database, otherwise the write will
    be rejected as conflicting.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
