

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .azure_blob_fs_config import AzureBlobFsConfig
from .crypt_fs_config import CryptFsConfig
from .fs_providers import FsProviders
from .gcs_config import GcsConfig
from .http_fs_config import HttpFsConfig
from .os_fs_config import OsFsConfig
from .s3config import S3Config
from .sftp_fs_config import SftpFsConfig


class FilesystemConfig(UniversalBaseModel):
    """
    Storage filesystem details
    """

    provider: typing.Optional[FsProviders] = None
    osconfig: typing.Optional[OsFsConfig] = None
    s3config: typing.Optional[S3Config] = None
    gcsconfig: typing.Optional[GcsConfig] = None
    azblobconfig: typing.Optional[AzureBlobFsConfig] = None
    cryptconfig: typing.Optional[CryptFsConfig] = None
    sftpconfig: typing.Optional[SftpFsConfig] = None
    httpconfig: typing.Optional[HttpFsConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
