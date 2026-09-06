

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SearchOperatorString_BeginsWith(UniversalBaseModel):
    operator: typing.Literal["beginsWith"] = "beginsWith"
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorString_Contains(UniversalBaseModel):
    operator: typing.Literal["contains"] = "contains"
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorString_DoesNotBeginWith(UniversalBaseModel):
    operator: typing.Literal["doesNotBeginWith"] = "doesNotBeginWith"
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorString_DoesNotContain(UniversalBaseModel):
    operator: typing.Literal["doesNotContain"] = "doesNotContain"
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorString_DoesNotEndWith(UniversalBaseModel):
    operator: typing.Literal["doesNotEndWith"] = "doesNotEndWith"
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorString_EndsWith(UniversalBaseModel):
    operator: typing.Literal["endsWith"] = "endsWith"
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorString_Is(UniversalBaseModel):
    operator: typing.Literal["is"] = "is"
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorString_IsNot(UniversalBaseModel):
    operator: typing.Literal["isNot"] = "isNot"
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SearchOperatorString = typing_extensions.Annotated[
    typing.Union[
        SearchOperatorString_BeginsWith,
        SearchOperatorString_Contains,
        SearchOperatorString_DoesNotBeginWith,
        SearchOperatorString_DoesNotContain,
        SearchOperatorString_DoesNotEndWith,
        SearchOperatorString_EndsWith,
        SearchOperatorString_Is,
        SearchOperatorString_IsNot,
    ],
    pydantic.Field(discriminator="operator"),
]
