

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class SingleTypingResult_TypedClass(UniversalBaseModel):
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


class SingleTypingResult_TypedDict(UniversalBaseModel):
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


class SingleTypingResult_TypedObjectTypingResult(UniversalBaseModel):
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


class SingleTypingResult_TypedObjectWithValue(UniversalBaseModel):
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


class SingleTypingResult_TypedTaggedValue(UniversalBaseModel):
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


SingleTypingResult = typing_extensions.Annotated[
    typing.Union[
        SingleTypingResult_TypedClass,
        SingleTypingResult_TypedDict,
        SingleTypingResult_TypedObjectTypingResult,
        SingleTypingResult_TypedObjectWithValue,
        SingleTypingResult_TypedTaggedValue,
    ],
    pydantic.Field(discriminator="type"),
]
from .dict import Dict
from .map_typing_result import MapTypingResult
from .typed_dict import TypedDict
from .typed_null import TypedNull
from .typed_object_typing_result import TypedObjectTypingResult
from .typed_object_with_value import TypedObjectWithValue
from .typed_union import TypedUnion
from .typing_result import TypingResult
from .unknown import Unknown
from .typed_class import TypedClass

update_forward_refs(
    SingleTypingResult_TypedClass,
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
    SingleTypingResult_TypedDict,
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
    SingleTypingResult_TypedObjectTypingResult,
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
    SingleTypingResult_TypedObjectWithValue,
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
