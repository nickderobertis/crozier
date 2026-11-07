

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .map_node_test_case_validation_errors import MapNodeTestCaseValidationErrors
from .node_validation_error import NodeValidationError
from .node_validation_result_dto_expression_type import NodeValidationResultDtoExpressionType
from .ui_parameter import UiParameter


class NodeValidationResultDto(UniversalBaseModel):
    parameters: typing.Optional[typing.List[UiParameter]] = None
    expression_type: typing_extensions.Annotated[
        typing.Optional[NodeValidationResultDtoExpressionType],
        FieldMetadata(alias="expressionType"),
        pydantic.Field(alias="expressionType"),
    ] = None
    validation_errors: typing_extensions.Annotated[
        typing.Optional[typing.List[NodeValidationError]],
        FieldMetadata(alias="validationErrors"),
        pydantic.Field(alias="validationErrors"),
    ] = None
    validation_performed: typing_extensions.Annotated[
        bool, FieldMetadata(alias="validationPerformed"), pydantic.Field(alias="validationPerformed")
    ]
    test_cases_validation_errors: typing_extensions.Annotated[
        typing.Optional[MapNodeTestCaseValidationErrors],
        FieldMetadata(alias="testCasesValidationErrors"),
        pydantic.Field(alias="testCasesValidationErrors"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(NodeValidationResultDto)
