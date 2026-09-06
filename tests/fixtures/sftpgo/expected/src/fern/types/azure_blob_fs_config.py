

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .azure_blob_fs_config_access_tier import AzureBlobFsConfigAccessTier
from .secret import Secret


class AzureBlobFsConfig(UniversalBaseModel):
    """
    Azure Blob Storage configuration details
    """

    container: typing.Optional[str] = None
    account_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Storage Account Name, leave blank to use SAS URL
    """

    account_key: typing.Optional[Secret] = None
    sas_url: typing.Optional[Secret] = None
    endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    optional endpoint. Default is "blob.core.windows.net". If you use the emulator the endpoint must include the protocol, for example "http://127.0.0.1:10000"
    """

    upload_part_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    the buffer size (in MB) to use for multipart uploads. If this value is set to zero, the default value (5MB) will be used.
    """

    upload_concurrency: typing.Optional[int] = pydantic.Field(default=None)
    """
    the number of parts to upload in parallel. If this value is set to zero, the default value (5) will be used
    """

    download_part_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    the buffer size (in MB) to use for multipart downloads. If this value is set to zero, the default value (5MB) will be used.
    """

    download_concurrency: typing.Optional[int] = pydantic.Field(default=None)
    """
    the number of parts to download in parallel. If this value is set to zero, the default value (5) will be used
    """

    access_tier: typing.Optional[AzureBlobFsConfigAccessTier] = None
    key_prefix: typing.Optional[str] = pydantic.Field(default=None)
    """
    key_prefix is similar to a chroot directory for a local filesystem. If specified the user will only see contents that starts with this prefix and so you can restrict access to a specific virtual folder. The prefix is normalized on save: a leading "/" is removed and a trailing "/" is added; a non-empty value that resolves to the storage root is rejected. If empty the whole container contents will be available
    """

    use_emulator: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
