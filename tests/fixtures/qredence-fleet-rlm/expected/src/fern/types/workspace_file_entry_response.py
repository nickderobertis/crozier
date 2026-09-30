

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workspace_file_entry_response_kind import WorkspaceFileEntryResponseKind


class WorkspaceFileEntryResponse(UniversalBaseModel):
    path: str
    kind: WorkspaceFileEntryResponseKind
    byte_size: typing.Optional[int] = None
    modified_at: typing.Optional[str] = None
    checksum_sha256: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
