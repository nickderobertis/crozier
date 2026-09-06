

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .filesystem_config import FilesystemConfig


class BaseVirtualFolder(UniversalBaseModel):
    """
    Defines the filesystem for the virtual folder and the used quota limits. The same folder can be shared among multiple users and each user can have different quota limits or a different virtual path.
    """

    id: typing.Optional[int] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    unique name for this virtual folder
    """

    mapped_path: typing.Optional[str] = pydantic.Field(default=None)
    """
    absolute filesystem path to use as virtual folder
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    optional description
    """

    used_quota_size: typing.Optional[int] = None
    used_quota_files: typing.Optional[int] = None
    last_quota_update: typing.Optional[int] = pydantic.Field(default=None)
    """
    Last quota update as unix timestamp in milliseconds
    """

    users: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    list of usernames associated with this virtual folder
    """

    filesystem: typing.Optional[FilesystemConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
