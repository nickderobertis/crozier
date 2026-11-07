

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .json_exception_result import JsonExceptionResult
from .map_node_id_v import MapNodeIdV
from .node_transition_result import NodeTransitionResult


class TestResultsDto(UniversalBaseModel):
    node_results: typing_extensions.Annotated[
        typing.Optional[MapNodeIdV], FieldMetadata(alias="nodeResults"), pydantic.Field(alias="nodeResults")
    ] = None
    node_transition_results: typing_extensions.Annotated[
        typing.Optional[typing.List[NodeTransitionResult]],
        FieldMetadata(alias="nodeTransitionResults"),
        pydantic.Field(alias="nodeTransitionResults"),
    ] = None
    expression_evaluation_results: typing_extensions.Annotated[
        MapNodeIdV,
        FieldMetadata(alias="expressionEvaluationResults"),
        pydantic.Field(alias="expressionEvaluationResults"),
    ]
    external_service_invocation_results: typing_extensions.Annotated[
        MapNodeIdV,
        FieldMetadata(alias="externalServiceInvocationResults"),
        pydantic.Field(alias="externalServiceInvocationResults"),
    ]
    exceptions: typing.Optional[typing.List[JsonExceptionResult]] = None
    exceptions_by_node_id: typing_extensions.Annotated[
        MapNodeIdV, FieldMetadata(alias="exceptionsByNodeId"), pydantic.Field(alias="exceptionsByNodeId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
