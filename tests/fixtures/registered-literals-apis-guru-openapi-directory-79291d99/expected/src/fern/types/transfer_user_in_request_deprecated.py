

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transfer_user_address_in_request import TransferUserAddressInRequest


class TransferUserInRequestDeprecated(UniversalBaseModel):
    """
    The legal name and other information for the account holder.
    """

    address: typing.Optional[TransferUserAddressInRequest] = None
    email_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's email address.
    """

    legal_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's legal name.
    """

    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's phone number.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
