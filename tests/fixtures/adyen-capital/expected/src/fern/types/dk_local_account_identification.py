

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DkLocalAccountIdentification(UniversalBaseModel):
    account_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="accountNumber"),
        pydantic.Field(
            alias="accountNumber",
            description="The 4-10 digits bank account number (Kontonummer) (without separators or whitespace).",
        ),
    ]
    """
    The 4-10 digits bank account number (Kontonummer) (without separators or whitespace).
    """

    bank_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="bankCode"),
        pydantic.Field(
            alias="bankCode",
            description="The 4-digit bank code (Registreringsnummer) (without separators or whitespace).",
        ),
    ]
    """
    The 4-digit bank code (Registreringsnummer) (without separators or whitespace).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
