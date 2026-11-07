

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .rejected_transition_criterion_dto import RejectedTransitionCriterionDto
from .workflow_stop_reason_dto_type import WorkflowStopReasonDtoType


class WorkflowStopReasonDto(UniversalBaseModel):
    type: WorkflowStopReasonDtoType
    description: str = pydantic.Field()
    """
    Human-readable description of why the workflow stopped
    """

    rejected_transitions: typing_extensions.Annotated[
        typing.Optional[typing.List[RejectedTransitionCriterionDto]],
        FieldMetadata(alias="rejectedTransitions"),
        pydantic.Field(
            alias="rejectedTransitions",
            description="If stopped due to criteria rejections, the transitions that were rejected",
        ),
    ] = None
    """
    If stopped due to criteria rejections, the transitions that were rejected
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
