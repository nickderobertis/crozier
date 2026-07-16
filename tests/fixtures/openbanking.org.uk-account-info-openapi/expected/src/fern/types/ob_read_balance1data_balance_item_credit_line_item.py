

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_read_balance1data_balance_item_credit_line_item_amount import ObReadBalance1DataBalanceItemCreditLineItemAmount
from .ob_read_balance1data_balance_item_credit_line_item_type import ObReadBalance1DataBalanceItemCreditLineItemType


class ObReadBalance1DataBalanceItemCreditLineItem(UniversalBaseModel):
    """
    Set of elements used to provide details on the credit line.
    """

    amount: typing_extensions.Annotated[
        typing.Optional[ObReadBalance1DataBalanceItemCreditLineItemAmount], FieldMetadata(alias="Amount")
    ] = pydantic.Field(default=None)
    """
    Amount of money of the credit line.
    """

    included: typing_extensions.Annotated[bool, FieldMetadata(alias="Included")] = pydantic.Field()
    """
    Indicates whether or not the credit line is included in the balance of the account.
    Usage: If not present, credit line is not included in the balance amount of the account.
    """

    type: typing_extensions.Annotated[
        typing.Optional[ObReadBalance1DataBalanceItemCreditLineItemType], FieldMetadata(alias="Type")
    ] = pydantic.Field(default=None)
    """
    Limit type, in a coded form.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
