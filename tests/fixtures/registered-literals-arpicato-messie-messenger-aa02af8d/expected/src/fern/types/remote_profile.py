

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RemoteProfile(UniversalBaseModel):
    """
    The profile info of the logged-in user on the remote network.
    """

    phone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's phone number
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's email address
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's username
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's displayname
    """

    avatar: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's avatar
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
