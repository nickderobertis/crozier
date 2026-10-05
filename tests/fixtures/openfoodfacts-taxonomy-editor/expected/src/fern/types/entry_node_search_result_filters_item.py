

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .is_filter_search_term_filter_value import IsFilterSearchTermFilterValue


class EntryNodeSearchResultFiltersItem_Ancestor(UniversalBaseModel):
    filter_type: typing_extensions.Annotated[
        typing.Literal["ancestor"], FieldMetadata(alias="filterType"), pydantic.Field(alias="filterType")
    ] = "ancestor"
    filter_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="filterValue"), pydantic.Field(alias="filterValue")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNodeSearchResultFiltersItem_Child(UniversalBaseModel):
    filter_type: typing_extensions.Annotated[
        typing.Literal["child"], FieldMetadata(alias="filterType"), pydantic.Field(alias="filterType")
    ] = "child"
    filter_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="filterValue"), pydantic.Field(alias="filterValue")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNodeSearchResultFiltersItem_Descendant(UniversalBaseModel):
    filter_type: typing_extensions.Annotated[
        typing.Literal["descendant"], FieldMetadata(alias="filterType"), pydantic.Field(alias="filterType")
    ] = "descendant"
    filter_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="filterValue"), pydantic.Field(alias="filterValue")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNodeSearchResultFiltersItem_Is(UniversalBaseModel):
    filter_type: typing_extensions.Annotated[
        typing.Literal["is"], FieldMetadata(alias="filterType"), pydantic.Field(alias="filterType")
    ] = "is"
    filter_value: typing_extensions.Annotated[
        IsFilterSearchTermFilterValue, FieldMetadata(alias="filterValue"), pydantic.Field(alias="filterValue")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNodeSearchResultFiltersItem_Language(UniversalBaseModel):
    filter_type: typing_extensions.Annotated[
        typing.Literal["language"], FieldMetadata(alias="filterType"), pydantic.Field(alias="filterType")
    ] = "language"
    filter_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="filterValue"), pydantic.Field(alias="filterValue")
    ]
    negated: typing.Optional[bool] = None
    language: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNodeSearchResultFiltersItem_Parent(UniversalBaseModel):
    filter_type: typing_extensions.Annotated[
        typing.Literal["parent"], FieldMetadata(alias="filterType"), pydantic.Field(alias="filterType")
    ] = "parent"
    filter_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="filterValue"), pydantic.Field(alias="filterValue")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EntryNodeSearchResultFiltersItem_Property(UniversalBaseModel):
    filter_type: typing_extensions.Annotated[
        typing.Literal["property"], FieldMetadata(alias="filterType"), pydantic.Field(alias="filterType")
    ] = "property"
    filter_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="filterValue"), pydantic.Field(alias="filterValue")
    ]
    negated: typing.Optional[bool] = None
    inherited: typing.Optional[bool] = None
    property_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="propertyName"), pydantic.Field(alias="propertyName")
    ] = None
    property_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="propertyValue"), pydantic.Field(alias="propertyValue")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


EntryNodeSearchResultFiltersItem = typing_extensions.Annotated[
    typing.Union[
        EntryNodeSearchResultFiltersItem_Ancestor,
        EntryNodeSearchResultFiltersItem_Child,
        EntryNodeSearchResultFiltersItem_Descendant,
        EntryNodeSearchResultFiltersItem_Is,
        EntryNodeSearchResultFiltersItem_Language,
        EntryNodeSearchResultFiltersItem_Parent,
        EntryNodeSearchResultFiltersItem_Property,
    ],
    pydantic.Field(discriminator="filter_type"),
]
