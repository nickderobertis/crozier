

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_virtual_folder import BaseVirtualFolder


class VirtualFolder(BaseVirtualFolder):
    """
    A virtual folder is a mapping between a SFTPGo virtual path and a filesystem path outside the user home directory. The specified paths must be absolute and the virtual path cannot be "/", it must be a sub directory. The parent directory for the specified virtual path must exist. SFTPGo will try to automatically create any missing parent directory for the configured virtual folders at user login.
    """

    virtual_path: str
    quota_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Quota as size in bytes. 0 means unlimited, -1 means included in user quota. Quota applies to the whole folder, so every mapping of the same folder uses the same limits. Please note that quota is updated if files are added/removed via SFTPGo otherwise a quota scan or a manual quota update is needed
    """

    quota_files: typing.Optional[int] = pydantic.Field(default=None)
    """
    Quota as number of files. 0 means unlimited, -1 means included in user quota. Quota applies to the whole folder, so every mapping of the same folder uses the same limits. Please note that quota is updated if files are added/removed via SFTPGo otherwise a quota scan or a manual quota update is needed
    """

    subpath: typing.Optional[str] = pydantic.Field(default=None)
    """
    Re-roots the mapping: the mount at `virtual_path` serves the folder starting from this sub-path. Canonical POSIX path with a leading slash. Supported for local, encrypted, S3, GCS, Azure Blob and SFTP folders. On group mappings the `%username%` and `%role%` placeholders are supported.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
