

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workspace_file_entry_response import WorkspaceFileEntryResponse


class WorkspaceFileListResponse(UniversalBaseModel):
    entries: typing.List[WorkspaceFileEntryResponse]
    truncated: typing.Optional[bool] = None
    next_cursor: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
