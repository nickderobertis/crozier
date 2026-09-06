

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .group_user_settings import GroupUserSettings
from .virtual_folder import VirtualFolder


class Group(UniversalBaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    name is unique
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    optional description
    """

    created_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    creation time as unix timestamp in milliseconds
    """

    updated_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    last update time as unix timestamp in milliseconds
    """

    user_settings: typing.Optional[GroupUserSettings] = None
    virtual_folders: typing.Optional[typing.List[VirtualFolder]] = pydantic.Field(default=None)
    """
    mapping between virtual SFTPGo paths and folders
    """

    users: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    list of usernames associated with this group
    """

    admins: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    list of admins usernames associated with this group
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
