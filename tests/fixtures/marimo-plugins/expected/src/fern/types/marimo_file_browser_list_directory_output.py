

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_file_browser_list_directory_output_files_item import MarimoFileBrowserListDirectoryOutputFilesItem


class MarimoFileBrowserListDirectoryOutput(UniversalBaseModel):
    files: typing.List[MarimoFileBrowserListDirectoryOutputFilesItem]
    total_count: float
    is_truncated: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
