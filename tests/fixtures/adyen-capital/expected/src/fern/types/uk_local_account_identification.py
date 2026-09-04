

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UkLocalAccountIdentification(UniversalBaseModel):
    account_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="accountNumber"),
        pydantic.Field(
            alias="accountNumber", description="The 8-digit bank account number, without separators or whitespace."
        ),
    ]
    """
    The 8-digit bank account number, without separators or whitespace.
    """

    sort_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="sortCode"),
        pydantic.Field(
            alias="sortCode",
            description="The 6-digit [sort code](https://en.wikipedia.org/wiki/Sort_code), without separators or whitespace.",
        ),
    ]
    """
    The 6-digit [sort code](https://en.wikipedia.org/wiki/Sort_code), without separators or whitespace.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
