

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FolderRetention(UniversalBaseModel):
    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    virtual directory path as seen by users, if no other specific retention is defined, the retention applies for sub directories too. For example if retention is defined for the paths "/" and "/sub" then the retention for "/" is applied for any file outside the "/sub" directory
    """

    retention: typing.Optional[int] = pydantic.Field(default=None)
    """
    retention time in hours. All the files with a modification time older than the defined value will be deleted. 0 means exclude this path
    """

    delete_empty_dirs: typing.Optional[bool] = pydantic.Field(default=None)
    """
    if enabled, empty directories will be deleted
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
