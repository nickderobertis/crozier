

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_stats import FileStats


class SourceStats(UniversalBaseModel):
    """
    Aggregated metadata for a source
    """

    source_id: str = pydantic.Field()
    """
    Deprecated: Use `folder_id` field instead. Unique identifier of the source
    """

    source_name: str = pydantic.Field()
    """
    Deprecated: Use `folder_name` field instead. Name of the source
    """

    file_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of files in the source
    """

    total_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total size of all files in bytes
    """

    files: typing.Optional[typing.List[FileStats]] = pydantic.Field(default=None)
    """
    List of file statistics
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
