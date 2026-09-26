

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_part_source_text import FilePartSourceText
from .range import Range


class SymbolSource(UniversalBaseModel):
    text: FilePartSourceText
    path: str
    range: Range
    name: str
    kind: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
