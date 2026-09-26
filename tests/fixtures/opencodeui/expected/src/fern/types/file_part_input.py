

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_part_source import FilePartSource


class FilePartInput(UniversalBaseModel):
    id: typing.Optional[str] = None
    mime: str
    filename: typing.Optional[str] = None
    url: str
    source: typing.Optional[FilePartSource] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
