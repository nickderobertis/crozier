

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SearchOperatorEqualityNullableString_Is(UniversalBaseModel):
    operator: typing.Literal["is"] = "is"
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorEqualityNullableString_IsNot(UniversalBaseModel):
    operator: typing.Literal["isNot"] = "isNot"
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorEqualityNullableString_IsNotNull(UniversalBaseModel):
    operator: typing.Literal["isNotNull"] = "isNotNull"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorEqualityNullableString_IsNull(UniversalBaseModel):
    operator: typing.Literal["isNull"] = "isNull"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SearchOperatorEqualityNullableString = typing_extensions.Annotated[
    typing.Union[
        SearchOperatorEqualityNullableString_Is,
        SearchOperatorEqualityNullableString_IsNot,
        SearchOperatorEqualityNullableString_IsNotNull,
        SearchOperatorEqualityNullableString_IsNull,
    ],
    pydantic.Field(discriminator="operator"),
]
