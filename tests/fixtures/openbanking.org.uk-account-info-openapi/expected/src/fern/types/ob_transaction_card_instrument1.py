

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_transaction_card_instrument1authorisation_type import ObTransactionCardInstrument1AuthorisationType
from .ob_transaction_card_instrument1card_scheme_name import ObTransactionCardInstrument1CardSchemeName


class ObTransactionCardInstrument1(UniversalBaseModel):
    """
    Set of elements to describe the card instrument used in the transaction.
    """

    authorisation_type: typing_extensions.Annotated[
        typing.Optional[ObTransactionCardInstrument1AuthorisationType], FieldMetadata(alias="AuthorisationType")
    ] = pydantic.Field(default=None)
    """
    The card authorisation type.
    """

    card_scheme_name: typing_extensions.Annotated[
        ObTransactionCardInstrument1CardSchemeName, FieldMetadata(alias="CardSchemeName")
    ] = pydantic.Field()
    """
    Name of the card scheme.
    """

    identification: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Identification")] = (
        pydantic.Field(default=None)
    )
    """
    Identification assigned by an institution to identify the card instrument used in the transaction. This identification is known by the account owner, and may be masked.
    """

    name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Name")] = pydantic.Field(default=None)
    """
    Name of the cardholder using the card instrument.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
