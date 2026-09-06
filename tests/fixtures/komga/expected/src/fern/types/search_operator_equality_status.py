

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SearchOperatorEqualityStatus_Is(UniversalBaseModel):
    operator: typing.Literal["is"] = "is"
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorEqualityStatus_IsNot(UniversalBaseModel):
    operator: typing.Literal["isNot"] = "isNot"
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SearchOperatorEqualityStatus = typing_extensions.Annotated[
    typing.Union[SearchOperatorEqualityStatus_Is, SearchOperatorEqualityStatus_IsNot],
    pydantic.Field(discriminator="operator"),
]
