

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ca_local_bank_account_type import CaLocalBankAccountType


class CaLocalAccountIdentification(UniversalBaseModel):
    account_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="accountNumber"),
        pydantic.Field(
            alias="accountNumber",
            description="The 5- to 12-digit bank account number, without separators or whitespace.",
        ),
    ]
    """
    The 5- to 12-digit bank account number, without separators or whitespace.
    """

    account_type: typing_extensions.Annotated[
        typing.Optional[CaLocalBankAccountType],
        FieldMetadata(alias="accountType"),
        pydantic.Field(
            alias="accountType",
            description="The bank account type.\n\nPossible values: **checking** or **savings**. Defaults to **checking**.",
        ),
    ] = None
    """
    The bank account type.
    
    Possible values: **checking** or **savings**. Defaults to **checking**.
    """

    institution_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="institutionNumber"),
        pydantic.Field(
            alias="institutionNumber", description="The 3-digit institution number, without separators or whitespace."
        ),
    ]
    """
    The 3-digit institution number, without separators or whitespace.
    """

    transit_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="transitNumber"),
        pydantic.Field(
            alias="transitNumber", description="The 5-digit transit number, without separators or whitespace."
        ),
    ]
    """
    The 5-digit transit number, without separators or whitespace.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
