

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class TestCaseAdditionalVariablesResponseDto(UniversalBaseModel):
    assertions_additional_variables: typing_extensions.Annotated[
        "MapTypingResult",
        FieldMetadata(alias="assertionsAdditionalVariables"),
        pydantic.Field(alias="assertionsAdditionalVariables"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .dict import Dict
from .map_typing_result import MapTypingResult
from .single_typing_result import SingleTypingResult
from .typed_class import TypedClass
from .typed_dict import TypedDict
from .typed_null import TypedNull
from .typed_object_typing_result import TypedObjectTypingResult
from .typed_object_with_value import TypedObjectWithValue
from .typed_union import TypedUnion
from .typing_result import TypingResult
from .unknown import Unknown

update_forward_refs(
    TestCaseAdditionalVariablesResponseDto,
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
    Unknown=Unknown,
)
