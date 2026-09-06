

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class SearchConditionComplete(UniversalBaseModel):
    complete: "SearchOperatorBoolean"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .search_operator_boolean import SearchOperatorBoolean
from .search_operator_is_false import SearchOperatorIsFalse
from .search_operator_is_true import SearchOperatorIsTrue

update_forward_refs(
    SearchConditionComplete,
    SearchOperatorBoolean=SearchOperatorBoolean,
    SearchOperatorIsFalse=SearchOperatorIsFalse,
    SearchOperatorIsTrue=SearchOperatorIsTrue,
)
