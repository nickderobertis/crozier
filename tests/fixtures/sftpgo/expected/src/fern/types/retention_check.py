

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .folder_retention import FolderRetention


class RetentionCheck(UniversalBaseModel):
    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    username to which the retention check refers
    """

    folders: typing.Optional[typing.List[FolderRetention]] = None
    start_time: typing.Optional[int] = pydantic.Field(default=None)
    """
    check start time as unix timestamp in milliseconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
