

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .filtered_file import FilteredFile


class PostSearchResponse(UniversalBaseModel):
    files: typing.List[FilteredFile]
    folders: typing.List["FilteredFolder"]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .filtered_folder import FilteredFolder

update_forward_refs(PostSearchResponse, FilteredFolder=FilteredFolder)
