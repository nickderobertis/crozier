

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BankAccount(UniversalBaseModel):
    account_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AccountName"),
        pydantic.Field(alias="AccountName", description="The name of the account"),
    ] = None
    """
    The name of the account
    """

    account_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AccountNumber"),
        pydantic.Field(alias="AccountNumber", description="The account number"),
    ] = None
    """
    The account number
    """

    amount: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Amount"),
        pydantic.Field(
            alias="Amount",
            description="Fixed amounts (for example, if an employee wants to have $100 of their salary transferred to one account, and the remaining amount to another)",
        ),
    ] = None
    """
    Fixed amounts (for example, if an employee wants to have $100 of their salary transferred to one account, and the remaining amount to another)
    """

    bsb: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="BSB"),
        pydantic.Field(alias="BSB", description="The BSB number of the account"),
    ] = None
    """
    The BSB number of the account
    """

    remainder: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Remainder"),
        pydantic.Field(alias="Remainder", description="If this account is the Remaining bank account"),
    ] = None
    """
    If this account is the Remaining bank account
    """

    statement_text: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StatementText"),
        pydantic.Field(
            alias="StatementText",
            description="The text that will appear on your employee's bank statement when they receive payment",
        ),
    ] = None
    """
    The text that will appear on your employee's bank statement when they receive payment
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
