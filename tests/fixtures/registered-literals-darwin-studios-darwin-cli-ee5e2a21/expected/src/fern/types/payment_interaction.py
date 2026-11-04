

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .payment_interaction_kind import PaymentInteractionKind
from .payment_interaction_payment import PaymentInteractionPayment
from .payment_interaction_state import PaymentInteractionState


class PaymentInteraction(UniversalBaseModel):
    id: str
    kind: PaymentInteractionKind
    state: PaymentInteractionState
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    hostname: str
    expires_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ]
    payment: PaymentInteractionPayment

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
