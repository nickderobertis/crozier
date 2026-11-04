

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .payment_interaction_payment_items_item import PaymentInteractionPaymentItemsItem
from .payment_interaction_payment_protocol import PaymentInteractionPaymentProtocol


class PaymentInteractionPayment(UniversalBaseModel):
    amount_minor: typing_extensions.Annotated[
        int, FieldMetadata(alias="amountMinor"), pydantic.Field(alias="amountMinor")
    ]
    currency: str
    items: typing.List[PaymentInteractionPaymentItemsItem]
    fees_minor: typing_extensions.Annotated[int, FieldMetadata(alias="feesMinor"), pydantic.Field(alias="feesMinor")]
    protocol: PaymentInteractionPaymentProtocol
    checkout_revision: typing_extensions.Annotated[
        str, FieldMetadata(alias="checkoutRevision"), pydantic.Field(alias="checkoutRevision")
    ]
    checkout_digest: typing_extensions.Annotated[
        str, FieldMetadata(alias="checkoutDigest"), pydantic.Field(alias="checkoutDigest")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
