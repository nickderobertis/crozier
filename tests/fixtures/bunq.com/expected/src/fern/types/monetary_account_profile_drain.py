

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .label_monetary_account import LabelMonetaryAccount


class MonetaryAccountProfileDrain(UniversalBaseModel):
    balance_preferred: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The goal balance.
    """

    balance_threshold_high: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The high threshold balance.
    """

    savings_account_alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The savings monetary account.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the profile.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
