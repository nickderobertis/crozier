

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TransferBalanceResponse(UniversalBaseModel):
    amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Balance transfer amount
    """

    balance_transfer_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique balance transfer ID
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date and time when the balance transfer was executed
    """

    from_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="Account the balance is transferred from"),
    ] = None
    """
    Account the balance is transferred from
    """

    reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reference for the balance transfer
    """

    to: typing.Optional[str] = pydantic.Field(default=None)
    """
    Account the balance is transferred to
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
