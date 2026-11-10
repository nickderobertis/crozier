

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .deposit_switch_get_response_state import DepositSwitchGetResponseState
from .deposit_switch_get_response_switch_method import DepositSwitchGetResponseSwitchMethod
from .request_id import RequestId


class DepositSwitchGetResponse(UniversalBaseModel):
    """
    DepositSwitchGetResponse defines the response schema for `/deposit_switch/get`
    """

    account_has_multiple_allocations: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When `true`, user’s direct deposit goes to multiple banks. When false, user’s direct deposit only goes to the target account. Always `null` if the deposit switch has not been completed.
    """

    amount_allocated: typing.Optional[float] = pydantic.Field(default=None)
    """
    The dollar amount of direct deposit allocated to the target account. Always `null` if the target account is not allocated an amount or if the deposit switch has not been completed.
    """

    date_completed: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    [ISO 8601](https://wikipedia.org/wiki/ISO_8601) date the deposit switch was completed. Always `null` if the deposit switch has not been completed.
    """

    date_created: dt.date = pydantic.Field()
    """
    [ISO 8601](https://wikipedia.org/wiki/ISO_8601) date the deposit switch was created.
    """

    deposit_switch_id: str = pydantic.Field()
    """
    The ID of the deposit switch.
    """

    employer_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the employer selected by the user. If the user did not select an employer, the value returned is `null`.
    """

    employer_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the employer selected by the user. If the user did not select an employer, the value returned is `null`.
    """

    institution_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the institution selected by the user. If the user did not select an institution, the value returned is `null`.
    """

    institution_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the institution selected by the user. If the user did not select an institution, the value returned is `null`.
    """

    is_allocated_remainder: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When `true`, the target account is allocated the remainder of direct deposit after all other allocations have been deducted. When `false`, user’s direct deposit is allocated as a percent or amount. Always `null` if the deposit switch has not been completed.
    """

    percent_allocated: typing.Optional[float] = pydantic.Field(default=None)
    """
    The percentage of direct deposit allocated to the target account. Always `null` if the target account is not allocated a percentage or if the deposit switch has not been completed or if `is_allocated_remainder` is true.
    """

    request_id: RequestId
    state: DepositSwitchGetResponseState = pydantic.Field()
    """
    
    The state, or status, of the deposit switch.
    
    - `initialized` – The deposit switch has been initialized with the user entering the information required to submit the deposit switch request.
    
    - `processing` – The deposit switch request has been submitted and is being processed.
    
    - `completed` – The user's employer has fulfilled the deposit switch request.
    
    - `error` – There was an error processing the deposit switch request.
    """

    switch_method: typing.Optional[DepositSwitchGetResponseSwitchMethod] = pydantic.Field(default=None)
    """
    The method used to make the deposit switch.
    
    - `instant` – User instantly switched their direct deposit to a new or existing bank account by connecting their payroll or employer account.
    
    - `mail` – User requested that Plaid contact their employer by mail to make the direct deposit switch.
    
    - `pdf` – User generated a PDF or email to be sent to their employer with the information necessary to make the deposit switch.'
    """

    target_account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the bank account the direct deposit was switched to.
    """

    target_item_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the Item the direct deposit was switched to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
