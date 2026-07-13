

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .monetary_account_profile_drain import MonetaryAccountProfileDrain
from .monetary_account_profile_fill import MonetaryAccountProfileFill


class MonetaryAccountProfile(UniversalBaseModel):
    profile_drain: typing.Optional[MonetaryAccountProfileDrain] = pydantic.Field(default=None)
    """
    The profile settings for moving excesses to a savings account
    """

    profile_fill: typing.Optional[MonetaryAccountProfileFill] = pydantic.Field(default=None)
    """
    The profile settings for triggering the fill of a monetary account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
