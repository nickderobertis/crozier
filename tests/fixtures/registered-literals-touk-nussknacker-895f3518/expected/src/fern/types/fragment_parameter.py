

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .fixed_expression_value import FixedExpressionValue
from .fragment_clazz_ref import FragmentClazzRef
from .parameter_value_compile_time_validation import ParameterValueCompileTimeValidation
from .parameter_value_input import ParameterValueInput


class FragmentParameter(UniversalBaseModel):
    name: str
    typ: FragmentClazzRef
    required: bool
    initial_value: typing_extensions.Annotated[
        typing.Optional[FixedExpressionValue], FieldMetadata(alias="initialValue"), pydantic.Field(alias="initialValue")
    ] = None
    hint_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="hintText"), pydantic.Field(alias="hintText")
    ] = None
    value_editor: typing_extensions.Annotated[
        typing.Optional[ParameterValueInput], FieldMetadata(alias="valueEditor"), pydantic.Field(alias="valueEditor")
    ] = None
    value_compile_time_validation: typing_extensions.Annotated[
        typing.Optional[ParameterValueCompileTimeValidation],
        FieldMetadata(alias="valueCompileTimeValidation"),
        pydantic.Field(alias="valueCompileTimeValidation"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
