

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class FileUpdateResponse(UniversalBaseModel):
    info: typing.Optional["FileInfo"] = None
    message: typing.Optional[str] = None
    success: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .file_info import FileInfo

update_forward_refs(FileUpdateResponse, FileInfo=FileInfo)
