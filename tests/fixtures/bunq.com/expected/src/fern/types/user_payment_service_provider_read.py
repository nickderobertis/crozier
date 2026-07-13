

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .avatar import Avatar
from .pointer import Pointer


class UserPaymentServiceProviderRead(UniversalBaseModel):
    alias: typing.Optional[typing.List[Pointer]] = pydantic.Field(default=None)
    """
    The aliases of the user.
    """

    avatar: typing.Optional[Avatar] = pydantic.Field(default=None)
    """
    The user's avatar.
    """

    certificate_distinguished_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The distinguished name from the certificate used to identify this user.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the user object's creation.
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The display name for the provider.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the user.
    """

    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    The provider's language. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.
    """

    public_nick_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The public nick name for the provider.
    """

    public_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The providers's public UUID.
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The provider's region. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.
    """

    session_timeout: typing.Optional[int] = pydantic.Field(default=None)
    """
    The setting for the session timeout of the user in seconds.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user status. The user status. Can be: ACTIVE, BLOCKED or DENIED.
    """

    sub_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user sub-status. Can be: NONE
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the user object's last update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
