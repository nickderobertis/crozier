

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .base_user_filters import BaseUserFilters
from .filesystem_config import FilesystemConfig
from .permission import Permission


class GroupUserSettings(UniversalBaseModel):
    home_dir: typing.Optional[str] = None
    max_sessions: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum number of concurrent sessions and file transfers for the user. Under bursts of near-simultaneous connections, the count can briefly exceed the configured limit. 0 means unlimited
    """

    quota_size: typing.Optional[int] = None
    quota_files: typing.Optional[int] = None
    permissions: typing.Optional[typing.Dict[str, typing.List[Permission]]] = pydantic.Field(default=None)
    """
    hash map with directory as key and an array of permissions as value. Directories must be absolute paths, permissions for root directory ("/") are required
    """

    upload_bandwidth: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum upload bandwidth in KB/s per upload, 0 means unlimited
    """

    download_bandwidth: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum download bandwidth in KB/s per upload, 0 means unlimited
    """

    upload_data_transfer: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum data transfer allowed for uploads as MB
    """

    download_data_transfer: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum data transfer allowed for downloads as MB
    """

    total_data_transfer: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum total data transfer as MB
    """

    expires_in: typing.Optional[int] = pydantic.Field(default=None)
    """
    Account expiration in number of days from creation. 0 means no expiration
    """

    filters: typing.Optional[BaseUserFilters] = None
    filesystem: typing.Optional[FilesystemConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
