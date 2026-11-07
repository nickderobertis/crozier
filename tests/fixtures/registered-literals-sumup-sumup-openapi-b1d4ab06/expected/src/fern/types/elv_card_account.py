

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ElvCardAccount(UniversalBaseModel):
    """
    Details of the ELV card account associated with the transaction.
    """

    sort_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    ELV card sort code.
    """

    last4digits: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="last_4_digits"),
        pydantic.Field(alias="last_4_digits", description="ELV card account number last 4 digits."),
    ] = None
    """
    ELV card account number last 4 digits.
    """

    sequence_no: typing.Optional[int] = pydantic.Field(default=None)
    """
    ELV card sequence number.
    """

    iban: typing.Optional[str] = pydantic.Field(default=None)
    """
    ELV IBAN.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
