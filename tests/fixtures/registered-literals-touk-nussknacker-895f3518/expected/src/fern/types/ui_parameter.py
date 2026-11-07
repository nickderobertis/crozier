

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .expression import Expression
from .parameter_category import ParameterCategory
from .parameter_editor import ParameterEditor
from .ui_parameter_typ import UiParameterTyp


class UiParameter(UniversalBaseModel):
    name: str
    typ: typing.Optional[UiParameterTyp] = None
    editors: typing.Optional[typing.List[ParameterEditor]] = None
    default_value: typing_extensions.Annotated[
        Expression, FieldMetadata(alias="defaultValue"), pydantic.Field(alias="defaultValue")
    ]
    additional_variables: typing_extensions.Annotated[
        "MapTypingResult", FieldMetadata(alias="additionalVariables"), pydantic.Field(alias="additionalVariables")
    ]
    variables_to_hide: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="variablesToHide"),
        pydantic.Field(alias="variablesToHide"),
    ] = None
    branch_param: typing_extensions.Annotated[
        bool, FieldMetadata(alias="branchParam"), pydantic.Field(alias="branchParam")
    ]
    hint_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="hintText"), pydantic.Field(alias="hintText")
    ] = None
    label: str
    required_param: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="requiredParam"), pydantic.Field(alias="requiredParam")
    ] = None
    category: ParameterCategory
    changes_can_reload_parameters: typing_extensions.Annotated[
        bool, FieldMetadata(alias="changesCanReloadParameters"), pydantic.Field(alias="changesCanReloadParameters")
    ]
    non_important_for_execution: typing_extensions.Annotated[
        bool, FieldMetadata(alias="nonImportantForExecution"), pydantic.Field(alias="nonImportantForExecution")
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
from .typed_class import TypedClass
from .typed_dict import TypedDict
from .typed_null import TypedNull
from .typed_object_typing_result import TypedObjectTypingResult
from .typed_object_with_value import TypedObjectWithValue
from .typed_union import TypedUnion
from .unknown import Unknown
from .single_typing_result import SingleTypingResult
from .typing_result import TypingResult

update_forward_refs(
    UiParameter,
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
