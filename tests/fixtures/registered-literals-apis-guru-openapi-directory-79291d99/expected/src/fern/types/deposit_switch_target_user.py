

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .deposit_switch_address_data import DepositSwitchAddressData


class DepositSwitchTargetUser(UniversalBaseModel):
    """
    The deposit switch target user
    """

    address: typing.Optional[DepositSwitchAddressData] = None
    email: str = pydantic.Field()
    """
    The email address of the user.
    """

    family_name: str = pydantic.Field()
    """
    The family name (last name) of the user.
    """

    given_name: str = pydantic.Field()
    """
    The given name (first name) of the user.
    """

    phone: str = pydantic.Field()
    """
    The phone number of the user. The endpoint can accept a variety of phone number formats, including E.164.
    """

    tax_payer_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The taxpayer ID of the user, generally their SSN, EIN, or TIN.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
