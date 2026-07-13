

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .label_monetary_account import LabelMonetaryAccount
from .registry_membership import RegistryMembership


class RegistrySettlementItem(UniversalBaseModel):
    amount: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount of the RegistrySettlementItem.
    """

    membership_paying: typing.Optional[RegistryMembership] = pydantic.Field(default=None)
    """
    The membership of the user that has to pay.
    """

    membership_receiving: typing.Optional[RegistryMembership] = pydantic.Field(default=None)
    """
    The membership of the user that will receive money.
    """

    paying_user_alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The LabelMonetaryAccount of the user that has to pay the request.
    """

    receiving_user_alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The LabelMonetaryAccount of the user that will receive the amount.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
