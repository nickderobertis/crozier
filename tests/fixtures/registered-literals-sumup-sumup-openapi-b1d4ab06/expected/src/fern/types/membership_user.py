

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .membership_user_classic import MembershipUserClassic
from .user_type import UserType


class MembershipUser(UniversalBaseModel):
    """
    Information about the user associated with the membership.
    """

    id: str = pydantic.Field()
    """
    Identifier for the End-User (also called Subject).
    """

    type: UserType
    email: str = pydantic.Field()
    """
    End-User's preferred e-mail address. Its value MUST conform to the RFC 5322 [RFC5322] addr-spec syntax. The RP MUST NOT rely upon this value being unique, for unique identification use ID instead.
    """

    mfa_on_login_enabled: bool = pydantic.Field()
    """
    True if the user has enabled MFA on login.
    """

    virtual_user: bool = pydantic.Field()
    """
    True if the user is a virtual user (operator).
    """

    service_account_user: bool = pydantic.Field()
    """
    True if the user is a service account.
    """

    disabled_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Time when the user has been disabled. Applies only to virtual users (`virtual_user: true`).
    """

    nickname: typing.Optional[str] = pydantic.Field(default=None)
    """
    User's nickname. Used for display purposes only.
    """

    picture: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the End-User's profile picture. This URL refers to an image file (for example, a PNG, JPEG, or GIF image file), rather than to a Web page containing an image.
    """

    classic: typing.Optional[MembershipUserClassic] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
