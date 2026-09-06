

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .ecomm_order_changed_payload_payload_stripe_card_brand import EcommOrderChangedPayloadPayloadStripeCardBrand
from .ecomm_order_changed_payload_payload_stripe_card_expires import EcommOrderChangedPayloadPayloadStripeCardExpires


class EcommOrderChangedPayloadPayloadStripeCard(UniversalBaseModel):
    """
    Details on the card used to fulfill this order, if this order was finalized with Stripe.
    """

    last4: typing.Optional[str] = pydantic.Field(default=None)
    """
    The last 4 digits on the card as a string
    """

    brand: typing.Optional[EcommOrderChangedPayloadPayloadStripeCardBrand] = pydantic.Field(default=None)
    """
    The card's brand (ie. credit card network)
    """

    owner_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ownerName"),
        pydantic.Field(alias="ownerName", description="The name on the card."),
    ] = None
    """
    The name on the card.
    """

    expires: typing.Optional[EcommOrderChangedPayloadPayloadStripeCardExpires] = pydantic.Field(default=None)
    """
    The card's expiration date.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
