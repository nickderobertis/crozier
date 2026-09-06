

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class SearchOperatorDate_After(UniversalBaseModel):
    operator: typing.Literal["after"] = "after"
    date_time: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="dateTime"), pydantic.Field(alias="dateTime")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorDate_Before(UniversalBaseModel):
    operator: typing.Literal["before"] = "before"
    date_time: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="dateTime"), pydantic.Field(alias="dateTime")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorDate_IsInTheLast(UniversalBaseModel):
    operator: typing.Literal["isInTheLast"] = "isInTheLast"
    duration: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorDate_IsNotInTheLast(UniversalBaseModel):
    operator: typing.Literal["isNotInTheLast"] = "isNotInTheLast"
    duration: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchOperatorDate_IsNotNull(UniversalBaseModel):
    value: "SearchOperatorIsNotNull"
    operator: typing.Literal["isNotNull"] = "isNotNull"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


class SearchOperatorDate_IsNull(UniversalBaseModel):
    value: "SearchOperatorIsNull"
    operator: typing.Literal["isNull"] = "isNull"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


SearchOperatorDate = typing_extensions.Annotated[
    typing.Union[
        SearchOperatorDate_After,
        SearchOperatorDate_Before,
        SearchOperatorDate_IsInTheLast,
        SearchOperatorDate_IsNotInTheLast,
        SearchOperatorDate_IsNotNull,
        SearchOperatorDate_IsNull,
    ],
    pydantic.Field(discriminator="operator"),
]
from .search_operator_is_null import SearchOperatorIsNull
from .search_operator_is_not_null import SearchOperatorIsNotNull

update_forward_refs(
    SearchOperatorDate_IsNotNull,
    SearchOperatorDate=SearchOperatorDate,
    SearchOperatorIsNotNull=SearchOperatorIsNotNull,
    SearchOperatorIsNull=SearchOperatorIsNull,
)
update_forward_refs(
    SearchOperatorDate_IsNull,
    SearchOperatorDate=SearchOperatorDate,
    SearchOperatorIsNotNull=SearchOperatorIsNotNull,
    SearchOperatorIsNull=SearchOperatorIsNull,
)
