

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .deposit_switch_target_account_account_subtype import DepositSwitchTargetAccountAccountSubtype


class DepositSwitchTargetAccount(UniversalBaseModel):
    """
    The deposit switch destination account
    """

    account_name: str = pydantic.Field()
    """
    The name of the deposit switch destination account, as it will be displayed to the end user in the Deposit Switch interface. It is not required to match the name used in online banking.
    """

    account_number: str = pydantic.Field()
    """
    Account number for deposit switch destination
    """

    account_subtype: DepositSwitchTargetAccountAccountSubtype = pydantic.Field()
    """
    The account subtype of the account, either `checking` or `savings`.
    """

    routing_number: str = pydantic.Field()
    """
    Routing number for deposit switch destination
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
