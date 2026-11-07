

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .abstract_condition_dto import AbstractConditionDto
from .json_node import JsonNode
from .simple_condition_dto_operator_type import SimpleConditionDtoOperatorType


class SimpleConditionDto(AbstractConditionDto):
    json_path: typing_extensions.Annotated[str, FieldMetadata(alias="jsonPath"), pydantic.Field(alias="jsonPath")]
    operator_type: typing_extensions.Annotated[
        SimpleConditionDtoOperatorType, FieldMetadata(alias="operatorType"), pydantic.Field(alias="operatorType")
    ]
    value: JsonNode

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
