

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .recursive_types_linked_list_response_result import RecursiveTypesLinkedListResponseResult


class RecursiveTypesLinkedListResponse(UniversalBaseModel):
    result: RecursiveTypesLinkedListResponseResult

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(RecursiveTypesLinkedListResponse)
