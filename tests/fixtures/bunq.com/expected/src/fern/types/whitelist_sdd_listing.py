

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .label_monetary_account import LabelMonetaryAccount
from .label_user import LabelUser


class WhitelistSddListing(UniversalBaseModel):
    counterparty_alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The account to which payments will be paid.
    """

    credit_scheme_identifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    The credit scheme ID provided by the counterparty.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the whitelist entry.
    """

    mandate_identifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    The mandate ID provided by the counterparty.
    """

    maximum_amount_per_month: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The monthly maximum amount that can be deducted from the target account.
    """

    monetary_account_incoming_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The account to which payments will come in before possibly being 'redirected' by the whitelist.
    """

    monetary_account_paying_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The account from which payments will be deducted when a transaction is matched with this whitelist.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the whitelist.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the SDD whitelist, can be CORE or B2B.
    """

    user_alias_created: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The user who created the whitelist entry.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
