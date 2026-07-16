

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_type import AccountType


class Account(UniversalBaseModel):
    account_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="AccountID")] = pydantic.Field(
        default=None
    )
    """
    Xero identifier for accounts
    """

    code: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Code")] = pydantic.Field(default=None)
    """
    Customer defined account code
    """

    name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Name")] = pydantic.Field(default=None)
    """
    Name of account
    """

    type: typing_extensions.Annotated[typing.Optional[AccountType], FieldMetadata(alias="Type")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
