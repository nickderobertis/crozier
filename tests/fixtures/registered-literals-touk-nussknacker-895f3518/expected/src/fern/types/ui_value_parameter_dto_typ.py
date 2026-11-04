

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class UiValueParameterDtoTyp_TypedClass(UniversalBaseModel):
    type: typing.Literal["TypedClass"] = "TypedClass"
    display: typing.Optional[str] = None
    ref_clazz_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="refClazzName"), pydantic.Field(alias="refClazzName")
    ]
    params: typing.Optional[typing.List["TypingResult"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiValueParameterDtoTyp_TypedDict(UniversalBaseModel):
    type: typing.Literal["TypedDict"] = "TypedDict"
    display: typing.Optional[str] = None
    dict_: typing_extensions.Annotated["Dict", FieldMetadata(alias="dict"), pydantic.Field(alias="dict")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiValueParameterDtoTyp_TypedNull(UniversalBaseModel):
    type: typing.Literal["TypedNull"] = "TypedNull"
    display: typing.Optional[str] = None
    ref_clazz_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="refClazzName"), pydantic.Field(alias="refClazzName")
    ] = None
    params: typing.Optional[typing.List["TypingResult"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiValueParameterDtoTyp_TypedObjectTypingResult(UniversalBaseModel):
    type: typing.Literal["TypedObjectTypingResult"] = "TypedObjectTypingResult"
    display: typing.Optional[str] = None
    fields: "MapTypingResult"
    ref_clazz_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="refClazzName"), pydantic.Field(alias="refClazzName")
    ]
    params: typing.Optional[typing.List["TypingResult"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiValueParameterDtoTyp_TypedObjectWithValue(UniversalBaseModel):
    type: typing.Literal["TypedObjectWithValue"] = "TypedObjectWithValue"
    value: typing.Any
    display: typing.Optional[str] = None
    ref_clazz_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="refClazzName"), pydantic.Field(alias="refClazzName")
    ]
    params: typing.Optional[typing.List["TypingResult"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiValueParameterDtoTyp_TypedTaggedValue(UniversalBaseModel):
    type: typing.Literal["TypedTaggedValue"] = "TypedTaggedValue"
    tag: str
    display: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiValueParameterDtoTyp_TypedUnion(UniversalBaseModel):
    type: typing.Literal["TypedUnion"] = "TypedUnion"
    display: typing.Optional[str] = None
    union: typing.List["TypingResult"]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UiValueParameterDtoTyp_Unknown(UniversalBaseModel):
    type: typing.Literal["Unknown"] = "Unknown"
    display: typing.Optional[str] = None
    ref_clazz_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="refClazzName"), pydantic.Field(alias="refClazzName")
    ] = None
    params: typing.Optional[typing.List["TypingResult"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


UiValueParameterDtoTyp = typing_extensions.Annotated[
    typing.Union[
        UiValueParameterDtoTyp_TypedClass,
        UiValueParameterDtoTyp_TypedDict,
        UiValueParameterDtoTyp_TypedNull,
        UiValueParameterDtoTyp_TypedObjectTypingResult,
        UiValueParameterDtoTyp_TypedObjectWithValue,
        UiValueParameterDtoTyp_TypedTaggedValue,
        UiValueParameterDtoTyp_TypedUnion,
        UiValueParameterDtoTyp_Unknown,
    ],
    pydantic.Field(discriminator="type"),
]
from .dict import Dict
from .map_typing_result import MapTypingResult
from .single_typing_result import SingleTypingResult
from .typed_dict import TypedDict
from .typed_null import TypedNull
from .typed_object_typing_result import TypedObjectTypingResult
from .typed_object_with_value import TypedObjectWithValue
from .typed_union import TypedUnion
from .typing_result import TypingResult
from .unknown import Unknown
from .typed_class import TypedClass

update_forward_refs(
    UiValueParameterDtoTyp_TypedClass,
    Dict=Dict,
    MapTypingResult=MapTypingResult,
    SingleTypingResult=SingleTypingResult,
    TypedDict=TypedDict,
    TypedNull=TypedNull,
    TypedObjectTypingResult=TypedObjectTypingResult,
    TypedObjectWithValue=TypedObjectWithValue,
    TypedUnion=TypedUnion,
    TypingResult=TypingResult,
    Unknown=Unknown,
)
update_forward_refs(
    UiValueParameterDtoTyp_TypedDict,
    Dict=Dict,
    MapTypingResult=MapTypingResult,
    SingleTypingResult=SingleTypingResult,
    TypedClass=TypedClass,
    TypedNull=TypedNull,
    TypedObjectTypingResult=TypedObjectTypingResult,
    TypedObjectWithValue=TypedObjectWithValue,
    TypedUnion=TypedUnion,
    TypingResult=TypingResult,
    Unknown=Unknown,
)
update_forward_refs(
    UiValueParameterDtoTyp_TypedNull,
    Dict=Dict,
    MapTypingResult=MapTypingResult,
    SingleTypingResult=SingleTypingResult,
    TypedClass=TypedClass,
    TypedDict=TypedDict,
    TypedObjectTypingResult=TypedObjectTypingResult,
    TypedObjectWithValue=TypedObjectWithValue,
    TypedUnion=TypedUnion,
    TypingResult=TypingResult,
    Unknown=Unknown,
)
update_forward_refs(
    UiValueParameterDtoTyp_TypedObjectTypingResult,
    Dict=Dict,
    MapTypingResult=MapTypingResult,
    SingleTypingResult=SingleTypingResult,
    TypedClass=TypedClass,
    TypedDict=TypedDict,
    TypedNull=TypedNull,
    TypedObjectWithValue=TypedObjectWithValue,
    TypedUnion=TypedUnion,
    TypingResult=TypingResult,
    Unknown=Unknown,
)
update_forward_refs(
    UiValueParameterDtoTyp_TypedObjectWithValue,
    Dict=Dict,
    MapTypingResult=MapTypingResult,
    SingleTypingResult=SingleTypingResult,
    TypedClass=TypedClass,
    TypedDict=TypedDict,
    TypedNull=TypedNull,
    TypedObjectTypingResult=TypedObjectTypingResult,
    TypedUnion=TypedUnion,
    TypingResult=TypingResult,
    Unknown=Unknown,
)
update_forward_refs(
    UiValueParameterDtoTyp_TypedUnion,
    Dict=Dict,
    MapTypingResult=MapTypingResult,
    SingleTypingResult=SingleTypingResult,
    TypedClass=TypedClass,
    TypedDict=TypedDict,
    TypedNull=TypedNull,
    TypedObjectTypingResult=TypedObjectTypingResult,
    TypedObjectWithValue=TypedObjectWithValue,
    TypingResult=TypingResult,
    Unknown=Unknown,
)
update_forward_refs(
    UiValueParameterDtoTyp_Unknown,
    Dict=Dict,
    MapTypingResult=MapTypingResult,
    SingleTypingResult=SingleTypingResult,
    TypedClass=TypedClass,
    TypedDict=TypedDict,
    TypedNull=TypedNull,
    TypedObjectTypingResult=TypedObjectTypingResult,
    TypedObjectWithValue=TypedObjectWithValue,
    TypedUnion=TypedUnion,
    TypingResult=TypingResult,
)
