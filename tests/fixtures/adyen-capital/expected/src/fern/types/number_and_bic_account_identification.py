

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .additional_bank_identification import AdditionalBankIdentification


class NumberAndBicAccountIdentification(UniversalBaseModel):
    account_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="accountNumber"),
        pydantic.Field(
            alias="accountNumber",
            description="The bank account number, without separators or whitespace. The length and format depends on the bank or country.",
        ),
    ]
    """
    The bank account number, without separators or whitespace. The length and format depends on the bank or country.
    """

    additional_bank_identification: typing_extensions.Annotated[
        typing.Optional[AdditionalBankIdentification],
        FieldMetadata(alias="additionalBankIdentification"),
        pydantic.Field(
            alias="additionalBankIdentification",
            description="Additional identification codes of the bank. Some banks may require these identifiers for cross-border transfers.",
        ),
    ] = None
    """
    Additional identification codes of the bank. Some banks may require these identifiers for cross-border transfers.
    """

    bic: str = pydantic.Field()
    """
    The bank's 8- or 11-character BIC or SWIFT code.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
