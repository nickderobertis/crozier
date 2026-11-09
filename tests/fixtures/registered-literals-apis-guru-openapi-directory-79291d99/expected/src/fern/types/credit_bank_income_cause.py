

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_bank_income_error_type import CreditBankIncomeErrorType


class CreditBankIncomeCause(UniversalBaseModel):
    """
    An error object and associated `item_id` used to identify a specific Item and error when a batch operation operating on multiple Items has encountered an error in one of the Items.
    """

    display_message: str = pydantic.Field()
    """
    A user-friendly representation of the error code. null if the error is not related to user action.
    This may change over time and is not safe for programmatic use.
    """

    error_code: str = pydantic.Field()
    """
    We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues. Error fields will be `null` if no error has occurred.
    """

    error_message: str = pydantic.Field()
    """
    A developer-friendly representation of the error code. This may change over time and is not safe for programmatic use.
    """

    error_type: CreditBankIncomeErrorType
    item_id: str = pydantic.Field()
    """
    The `item_id` of the Item associated with this warning.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
