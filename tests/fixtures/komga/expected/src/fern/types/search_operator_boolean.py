

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class SearchOperatorBoolean_IsFalse(UniversalBaseModel):
    value: "SearchOperatorIsFalse"
    operator: typing.Literal["isFalse"] = "isFalse"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


class SearchOperatorBoolean_IsTrue(UniversalBaseModel):
    value: "SearchOperatorIsTrue"
    operator: typing.Literal["isTrue"] = "isTrue"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


SearchOperatorBoolean = typing_extensions.Annotated[
    typing.Union[SearchOperatorBoolean_IsFalse, SearchOperatorBoolean_IsTrue], pydantic.Field(discriminator="operator")
]
from .search_operator_is_true import SearchOperatorIsTrue
from .search_operator_is_false import SearchOperatorIsFalse

update_forward_refs(
    SearchOperatorBoolean_IsFalse,
    SearchOperatorBoolean=SearchOperatorBoolean,
    SearchOperatorIsFalse=SearchOperatorIsFalse,
    SearchOperatorIsTrue=SearchOperatorIsTrue,
)
update_forward_refs(
    SearchOperatorBoolean_IsTrue,
    SearchOperatorBoolean=SearchOperatorBoolean,
    SearchOperatorIsFalse=SearchOperatorIsFalse,
    SearchOperatorIsTrue=SearchOperatorIsTrue,
)
