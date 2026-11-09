

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NumbersAch(UniversalBaseModel):
    """
    Identifying information for transferring money to or from a US account via ACH or wire transfer.
    """

    account: str = pydantic.Field()
    """
    The ACH account number for the account.
    
    Note that when using OAuth with Chase Bank (`ins_56`), Chase will issue "tokenized" routing and account numbers, which are not the user's actual account and routing numbers. These tokenized numbers should work identically to normal account and routing numbers. The digits returned in the `mask` field will continue to reflect the actual account number, rather than the tokenized account number; for this reason, when displaying account numbers to the user to help them identify their account in your UI, always use the `mask` rather than truncating the `account` number. If a user revokes their permissions to your app, the tokenized numbers will continue to work for ACH deposits, but not withdrawals.
    """

    account_id: str = pydantic.Field()
    """
    The Plaid account ID associated with the account numbers
    """

    can_transfer_in: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the account supports ACH transfers into the account
    """

    can_transfer_out: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the account supports ACH transfers out of the account
    """

    routing: str = pydantic.Field()
    """
    The ACH routing number for the account. If the institution is `ins_56`, this may be a tokenized routing number. For more information, see the description of the `account` field.
    """

    wire_routing: typing.Optional[str] = pydantic.Field(default=None)
    """
    The wire transfer routing number for the account, if available
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
