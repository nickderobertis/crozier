

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .signal_address_data import SignalAddressData


class IncomeVerificationPrecheckUser(UniversalBaseModel):
    """
    Information about the user whose eligibility is being evaluated.
    """

    email_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's email address
    """

    first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's first name
    """

    home_address: typing.Optional[SignalAddressData] = None
    last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's last name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
