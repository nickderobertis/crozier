

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MonetaryAccountSetting(UniversalBaseModel):
    color: typing.Optional[str] = pydantic.Field(default=None)
    """
    The color chosen for the MonetaryAccount.
    """

    default_avatar_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the avatar. Can be either AVATAR_DEFAULT, AVATAR_CUSTOM or AVATAR_UNDETERMINED.
    """

    icon: typing.Optional[str] = pydantic.Field(default=None)
    """
    The icon chosen for the MonetaryAccount.
    """

    restriction_chat: typing.Optional[str] = pydantic.Field(default=None)
    """
    The chat restriction. Possible values are ALLOW_INCOMING or BLOCK_INCOMING
    """

    sdd_expiration_action: typing.Optional[str] = pydantic.Field(default=None)
    """
    The preference for this monetary account on whether to automatically accept or reject expiring SDDs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
