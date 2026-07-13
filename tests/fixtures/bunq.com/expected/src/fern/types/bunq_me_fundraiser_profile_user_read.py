

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attachment_public import AttachmentPublic
from .label_monetary_account import LabelMonetaryAccount
from .pointer import Pointer


class BunqMeFundraiserProfileUserRead(UniversalBaseModel):
    alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The LabelMonetaryAccount with the public information of the User and the MonetaryAccount that created the bunq.me fundraiser profile.
    """

    attachment: typing.Optional[AttachmentPublic] = pydantic.Field(default=None)
    """
    The attachment used for the background of the bunq.me fundraiser profile.
    """

    color: typing.Optional[str] = pydantic.Field(default=None)
    """
    The color chosen for the bunq.me fundraiser profile in hexadecimal format.
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    The currency of the MonetaryAccount that created the bunq.me fundraiser profile.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the bunq.me fundraiser profile.
    """

    monetary_account_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Id of the monetary account on which you want to receive bunq.me payments.
    """

    owner_user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Id of the user owning the profile.
    """

    pointer: typing.Optional[Pointer] = pydantic.Field(default=None)
    """
    The pointer (url) which will be used to access the bunq.me fundraiser profile.
    """

    redirect_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL which the user is sent to when a payment is completed.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the bunq.me fundraiser profile, can be ACTIVE or DEACTIVATED.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
