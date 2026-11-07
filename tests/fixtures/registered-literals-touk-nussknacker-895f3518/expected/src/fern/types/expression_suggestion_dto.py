

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .expression_suggestion_dto_ref_clazz import ExpressionSuggestionDtoRefClazz
from .parameter_dto import ParameterDto


class ExpressionSuggestionDto(UniversalBaseModel):
    method_name: typing_extensions.Annotated[str, FieldMetadata(alias="methodName"), pydantic.Field(alias="methodName")]
    ref_clazz: typing_extensions.Annotated[
        ExpressionSuggestionDtoRefClazz, FieldMetadata(alias="refClazz"), pydantic.Field(alias="refClazz")
    ]
    from_class: typing_extensions.Annotated[bool, FieldMetadata(alias="fromClass"), pydantic.Field(alias="fromClass")]
    description: typing.Optional[str] = None
    parameters: typing.Optional[typing.List[ParameterDto]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ExpressionSuggestionDto)
