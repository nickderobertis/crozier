

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class HkLocalAccountIdentification(UniversalBaseModel):
    account_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="accountNumber"),
        pydantic.Field(
            alias="accountNumber",
            description="The 9- to 17-digit bank account number, without separators or whitespace. Starts with the 3-digit branch code.",
        ),
    ]
    """
    The 9- to 17-digit bank account number, without separators or whitespace. Starts with the 3-digit branch code.
    """

    clearing_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="clearingCode"),
        pydantic.Field(
            alias="clearingCode", description="The 3-digit clearing code, without separators or whitespace."
        ),
    ]
    """
    The 3-digit clearing code, without separators or whitespace.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
