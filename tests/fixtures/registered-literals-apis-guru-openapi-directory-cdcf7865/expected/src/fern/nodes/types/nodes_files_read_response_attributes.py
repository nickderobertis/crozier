

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NodesFilesReadResponseAttributes(UniversalBaseModel):
    """
    The properties of the file entity.
    """

    checkout: typing.Optional[str] = pydantic.Field(default=None)
    """
    SOON TO BE DEPRECATED, see relationships checkout.
    """

    current_user_can_comment: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the current user is allowed to post comments.
    """

    current_version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version number of the file.
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the file was created, as an iso8601 formatted timestamp.
    """

    date_modified: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the file was last modified, as an iso8601 formatted timestamp.
    """

    delete_allowed: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not deletion of the file is allowed.
    """

    extra: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Extra information, contains `hashes` (`sha256`, `md5`) and `downloads` count.
    """

    guid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Global unique identifier (GUID) for this file (if one has been assigned).
    """

    kind: typing.Optional[str] = pydantic.Field(default=None)
    """
    The kind of files object it is (`file` or `folder`).
    """

    last_touched: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the file external metadata was last retrieved as an iso8601 formatted timestamp (does not apply to OSF Storage files).
    """

    materialized_path: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unix-style path to the file relative to the provider root.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the file
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier for this file entity for this project and storage provider.
    """

    provider: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the file provider (e.g., `osfstorage`)
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Size of the file in bytes.
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of strings that describe this file, as entered by project contributors.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
