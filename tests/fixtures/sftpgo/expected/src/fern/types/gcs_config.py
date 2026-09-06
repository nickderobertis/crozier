

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .secret import Secret


class GcsConfig(UniversalBaseModel):
    """
    Google Cloud Storage configuration details. The "credentials" field must be populated only when adding/updating a user. It will be always omitted, since there are sensitive data, when you search/get users
    """

    bucket: typing.Optional[str] = None
    credentials: typing.Optional[Secret] = None
    automatic_credentials: typing.Optional[int] = pydantic.Field(default=None)
    """
    Automatic credentials:
      * `0` - disabled, explicit credentials, using a JSON credentials file, must be provided. This is the default value if the field is null
      * `1` - enabled, we try to use the Application Default Credentials (ADC) strategy to find your application's credentials
    """

    storage_class: typing.Optional[str] = None
    acl: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ACL to apply to uploaded objects. Leave empty to use the default ACL. For more information and available ACLs, refer to the JSON API here: https://cloud.google.com/storage/docs/access-control/lists#predefined-acl
    """

    key_prefix: typing.Optional[str] = pydantic.Field(default=None)
    """
    key_prefix is similar to a chroot directory for a local filesystem. If specified the user will only see contents that starts with this prefix and so you can restrict access to a specific virtual folder. The prefix is normalized on save: a leading "/" is removed and a trailing "/" is added; a non-empty value that resolves to the storage root is rejected. If empty the whole bucket contents will be available
    """

    upload_part_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The buffer size (in MB) to use for multipart uploads. The default value is 16MB. 0 means use the default
    """

    upload_part_max_time: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum time allowed, in seconds, to upload a single chunk. The default value is 32. 0 means use the default
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
