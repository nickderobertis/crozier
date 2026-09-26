

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .find_text_response_item_lines import FindTextResponseItemLines
from .find_text_response_item_path import FindTextResponseItemPath
from .find_text_response_item_submatches_item import FindTextResponseItemSubmatchesItem


class FindTextResponseItem(UniversalBaseModel):
    path: FindTextResponseItemPath
    lines: FindTextResponseItemLines
    line_number: float
    absolute_offset: float
    submatches: typing.List[FindTextResponseItemSubmatchesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
