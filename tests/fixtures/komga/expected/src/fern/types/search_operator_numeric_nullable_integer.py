

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SearchOperatorNumericNullableInteger_GreaterThan(UniversalBaseModel):
    operator: typing.Literal["greaterThan"] = "greaterThan"
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorNumericNullableInteger_Is(UniversalBaseModel):
    operator: typing.Literal["is"] = "is"
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorNumericNullableInteger_IsNot(UniversalBaseModel):
    operator: typing.Literal["isNot"] = "isNot"
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorNumericNullableInteger_IsNotNull(UniversalBaseModel):
    operator: typing.Literal["isNotNull"] = "isNotNull"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorNumericNullableInteger_IsNull(UniversalBaseModel):
    operator: typing.Literal["isNull"] = "isNull"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorNumericNullableInteger_LessThan(UniversalBaseModel):
    operator: typing.Literal["lessThan"] = "lessThan"
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SearchOperatorNumericNullableInteger = typing_extensions.Annotated[
    typing.Union[
        SearchOperatorNumericNullableInteger_GreaterThan,
        SearchOperatorNumericNullableInteger_Is,
        SearchOperatorNumericNullableInteger_IsNot,
        SearchOperatorNumericNullableInteger_IsNotNull,
        SearchOperatorNumericNullableInteger_IsNull,
        SearchOperatorNumericNullableInteger_LessThan,
    ],
    pydantic.Field(discriminator="operator"),
]
