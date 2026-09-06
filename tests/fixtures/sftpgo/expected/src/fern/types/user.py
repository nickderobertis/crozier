

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .filesystem_config import FilesystemConfig
from .group_mapping import GroupMapping
from .permission import Permission
from .user_filters import UserFilters
from .virtual_folder import VirtualFolder


class User(UniversalBaseModel):
    id: typing.Optional[int] = None
    status: typing.Optional[int] = pydantic.Field(default=None)
    """
    status:
      * `0` user is disabled, login is not allowed
      * `1` user is enabled
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    username is unique
    """

    email: typing.Optional[str] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    optional description, for example the user full name
    """

    expiration_date: typing.Optional[int] = pydantic.Field(default=None)
    """
    expiration date as unix timestamp in milliseconds. An expired account cannot login. 0 means no expiration
    """

    password: typing.Optional[str] = pydantic.Field(default=None)
    """
    If the password has no known hashing algo prefix it will be stored, by default, using bcrypt, argon2id is supported too. You can send a password hashed as bcrypt ($2a$ prefix), argon2id, pbkdf2 or unix crypt and it will be stored as is. For security reasons this field is omitted when you search/get users
    """

    public_keys: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Public keys in OpenSSH format.
    """

    has_password: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the password is set
    """

    home_dir: typing.Optional[str] = pydantic.Field(default=None)
    """
    path to the user home directory. The user cannot upload or download files outside this directory. SFTPGo tries to automatically create this folder if missing. Must be an absolute path
    """

    virtual_folders: typing.Optional[typing.List[VirtualFolder]] = pydantic.Field(default=None)
    """
    mapping between virtual SFTPGo paths and virtual folders
    """

    uid: typing.Optional[int] = pydantic.Field(default=None)
    """
    if you run SFTPGo as root user, the created files and directories will be assigned to this uid. 0 means no change, the owner will be the user that runs SFTPGo. Ignored on windows
    """

    gid: typing.Optional[int] = pydantic.Field(default=None)
    """
    if you run SFTPGo as root user, the created files and directories will be assigned to this gid. 0 means no change, the group will be the one of the user that runs SFTPGo. Ignored on windows
    """

    max_sessions: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum number of concurrent sessions and file transfers for the user. Under bursts of near-simultaneous connections, the count can briefly exceed the configured limit. 0 means unlimited
    """

    quota_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Quota as size in bytes. 0 means unlimited. Please note that quota is updated if files are added/removed via SFTPGo otherwise a quota scan or a manual quota update is needed
    """

    quota_files: typing.Optional[int] = pydantic.Field(default=None)
    """
    Quota as number of files. 0 means unlimited. Please note that quota is updated if files are added/removed via SFTPGo otherwise a quota scan or a manual quota update is needed
    """

    permissions: typing.Optional[typing.Dict[str, typing.List[Permission]]] = pydantic.Field(default=None)
    """
    hash map with directory as key and an array of permissions as value. Directories must be absolute paths, permissions for root directory ("/") are required
    """

    used_quota_size: typing.Optional[int] = None
    used_quota_files: typing.Optional[int] = None
    last_quota_update: typing.Optional[int] = pydantic.Field(default=None)
    """
    Last quota update as unix timestamp in milliseconds
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
    Maximum data transfer allowed for uploads as MB. 0 means no limit
    """

    download_data_transfer: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum data transfer allowed for downloads as MB. 0 means no limit
    """

    total_data_transfer: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum total data transfer as MB. 0 means unlimited. You can set a total data transfer instead of the individual values for uploads and downloads
    """

    used_upload_data_transfer: typing.Optional[int] = pydantic.Field(default=None)
    """
    Uploaded size, as bytes, since the last reset
    """

    used_download_data_transfer: typing.Optional[int] = pydantic.Field(default=None)
    """
    Downloaded size, as bytes, since the last reset
    """

    created_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    creation time as unix timestamp in milliseconds. It will be 0 for users created before v2.2.0
    """

    updated_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    last update time as unix timestamp in milliseconds
    """

    last_login: typing.Optional[int] = pydantic.Field(default=None)
    """
    Last user login as unix timestamp in milliseconds. It is saved at most once every 10 minutes
    """

    first_download: typing.Optional[int] = pydantic.Field(default=None)
    """
    first download time as unix timestamp in milliseconds
    """

    first_upload: typing.Optional[int] = pydantic.Field(default=None)
    """
    first upload time as unix timestamp in milliseconds
    """

    last_password_change: typing.Optional[int] = pydantic.Field(default=None)
    """
    last password change time as unix timestamp in milliseconds
    """

    filters: typing.Optional[UserFilters] = None
    filesystem: typing.Optional[FilesystemConfig] = None
    additional_info: typing.Optional[str] = pydantic.Field(default=None)
    """
    Free form text field for external systems
    """

    groups: typing.Optional[typing.List[GroupMapping]] = None
    oidc_custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    This field is passed to the pre-login hook if custom OIDC token fields have been configured. Field values can be of any type (this is a free form object) and depend on the type of the configured OIDC token fields
    """

    role: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
