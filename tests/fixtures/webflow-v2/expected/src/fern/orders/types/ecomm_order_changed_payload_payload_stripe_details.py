

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class EcommOrderChangedPayloadPayloadStripeDetails(UniversalBaseModel):
    """
    An object with various Stripe IDs, useful for linking into the stripe dashboard.
    """

    subscription_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="subscriptionId"),
        pydantic.Field(alias="subscriptionId", description="Stripe-generated identifier for the Subscription"),
    ] = None
    """
    Stripe-generated identifier for the Subscription
    """

    payment_method: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="paymentMethod"),
        pydantic.Field(alias="paymentMethod", description="Stripe-generated identifier for the PaymentMethod used"),
    ] = None
    """
    Stripe-generated identifier for the PaymentMethod used
    """

    payment_intent_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="paymentIntentId"),
        pydantic.Field(
            alias="paymentIntentId", description="Stripe-generated identifier for the PaymentIntent, or null"
        ),
    ] = None
    """
    Stripe-generated identifier for the PaymentIntent, or null
    """

    customer_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="customerId"),
        pydantic.Field(alias="customerId", description="Stripe-generated customer identifier, or null"),
    ] = None
    """
    Stripe-generated customer identifier, or null
    """

    charge_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="chargeId"),
        pydantic.Field(alias="chargeId", description="Stripe-generated charge identifier, or null"),
    ] = None
    """
    Stripe-generated charge identifier, or null
    """

    dispute_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="disputeId"),
        pydantic.Field(alias="disputeId", description="Stripe-generated dispute identifier, or null"),
    ] = None
    """
    Stripe-generated dispute identifier, or null
    """

    refund_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="refundId"),
        pydantic.Field(alias="refundId", description="Stripe-generated refund identifier, or null"),
    ] = None
    """
    Stripe-generated refund identifier, or null
    """

    refund_reason: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="refundReason"),
        pydantic.Field(alias="refundReason", description="Stripe-generated refund reason, or null"),
    ] = None
    """
    Stripe-generated refund reason, or null
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
