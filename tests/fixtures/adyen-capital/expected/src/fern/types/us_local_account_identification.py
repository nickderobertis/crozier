

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .us_local_bank_account_type import UsLocalBankAccountType


class UsLocalAccountIdentification(UniversalBaseModel):
    account_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="accountNumber"),
        pydantic.Field(alias="accountNumber", description="The bank account number, without separators or whitespace."),
    ]
    """
    The bank account number, without separators or whitespace.
    """

    account_type: typing_extensions.Annotated[
        typing.Optional[UsLocalBankAccountType],
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

    routing_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="routingNumber"),
        pydantic.Field(
            alias="routingNumber",
            description="The 9-digit [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or whitespace.",
        ),
    ]
    """
    The 9-digit [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or whitespace.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
