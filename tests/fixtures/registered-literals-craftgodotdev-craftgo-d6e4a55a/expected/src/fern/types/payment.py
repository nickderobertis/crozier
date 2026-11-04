

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .non_empty_id import NonEmptyId
from .payment_method import PaymentMethod
from .safe_url import SafeUrl


class Payment(UniversalBaseModel):
    card_last4: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="cardLast4"), pydantic.Field(alias="cardLast4")
    ] = None
    method: PaymentMethod
    receipt_url: typing_extensions.Annotated[
        typing.Optional[SafeUrl], FieldMetadata(alias="receiptURL"), pydantic.Field(alias="receiptURL")
    ] = None
    reference_id: typing_extensions.Annotated[
        NonEmptyId, FieldMetadata(alias="referenceId"), pydantic.Field(alias="referenceId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
