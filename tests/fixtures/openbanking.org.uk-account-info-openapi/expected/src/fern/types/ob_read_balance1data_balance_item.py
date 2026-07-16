

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_id import AccountId
from .ob_balance_type1code import ObBalanceType1Code
from .ob_credit_debit_code2 import ObCreditDebitCode2
from .ob_read_balance1data_balance_item_amount import ObReadBalance1DataBalanceItemAmount
from .ob_read_balance1data_balance_item_credit_line_item import ObReadBalance1DataBalanceItemCreditLineItem


class ObReadBalance1DataBalanceItem(UniversalBaseModel):
    """
    Set of elements used to define the balance details.
    """

    account_id: typing_extensions.Annotated[
        AccountId, FieldMetadata(alias="AccountId"), pydantic.Field(alias="AccountId")
    ]
    amount: typing_extensions.Annotated[
        ObReadBalance1DataBalanceItemAmount,
        FieldMetadata(alias="Amount"),
        pydantic.Field(alias="Amount", description="Amount of money of the cash balance."),
    ]
    """
    Amount of money of the cash balance.
    """

    credit_debit_indicator: typing_extensions.Annotated[
        ObCreditDebitCode2, FieldMetadata(alias="CreditDebitIndicator"), pydantic.Field(alias="CreditDebitIndicator")
    ]
    credit_line: typing_extensions.Annotated[
        typing.Optional[typing.List[ObReadBalance1DataBalanceItemCreditLineItem]],
        FieldMetadata(alias="CreditLine"),
        pydantic.Field(alias="CreditLine"),
    ] = None
    date_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="DateTime"),
        pydantic.Field(
            alias="DateTime",
            description="Indicates the date (and time) of the balance.All dates in the JSON payloads are represented in ISO 8601 date-time format. \nAll date-time fields in responses must include the timezone. An example is below:\n2017-04-05T10:43:07+00:00",
        ),
    ]
    """
    Indicates the date (and time) of the balance.All dates in the JSON payloads are represented in ISO 8601 date-time format. 
    All date-time fields in responses must include the timezone. An example is below:
    2017-04-05T10:43:07+00:00
    """

    type: typing_extensions.Annotated[ObBalanceType1Code, FieldMetadata(alias="Type"), pydantic.Field(alias="Type")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
