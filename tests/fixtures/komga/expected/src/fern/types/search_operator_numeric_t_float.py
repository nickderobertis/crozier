

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SearchOperatorNumericTFloat_GreaterThan(UniversalBaseModel):
    operator: typing.Literal["greaterThan"] = "greaterThan"
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorNumericTFloat_Is(UniversalBaseModel):
    operator: typing.Literal["is"] = "is"
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorNumericTFloat_IsNot(UniversalBaseModel):
    operator: typing.Literal["isNot"] = "isNot"
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorNumericTFloat_LessThan(UniversalBaseModel):
    operator: typing.Literal["lessThan"] = "lessThan"
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SearchOperatorNumericTFloat = typing_extensions.Annotated[
    typing.Union[
        SearchOperatorNumericTFloat_GreaterThan,
        SearchOperatorNumericTFloat_Is,
        SearchOperatorNumericTFloat_IsNot,
        SearchOperatorNumericTFloat_LessThan,
    ],
    pydantic.Field(discriminator="operator"),
]
