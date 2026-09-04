

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BrLocalAccountIdentification(UniversalBaseModel):
    account_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="accountNumber"),
        pydantic.Field(alias="accountNumber", description="The bank account number, without separators or whitespace."),
    ]
    """
    The bank account number, without separators or whitespace.
    """

    bank_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="bankCode"),
        pydantic.Field(alias="bankCode", description="The 3-digit bank code, with leading zeros."),
    ]
    """
    The 3-digit bank code, with leading zeros.
    """

    branch_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="branchNumber"),
        pydantic.Field(
            alias="branchNumber", description="The bank account branch number, without separators or whitespace."
        ),
    ]
    """
    The bank account branch number, without separators or whitespace.
    """

    ispb: typing.Optional[str] = pydantic.Field(default=None)
    """
    The 8-digit ISPB, with leading zeros.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
