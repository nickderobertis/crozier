

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .card_type import CardType


class PaymentInstrumentResponseCard(UniversalBaseModel):
    """
    Details of the payment card.
    """

    last4digits: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="last_4_digits"),
        pydantic.Field(alias="last_4_digits", description="Last 4 digits of the payment card number."),
    ] = None
    """
    Last 4 digits of the payment card number.
    """

    type: typing.Optional[CardType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
