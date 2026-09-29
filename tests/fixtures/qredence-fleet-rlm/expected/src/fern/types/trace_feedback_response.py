

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .trace_feedback_response_name import TraceFeedbackResponseName


class TraceFeedbackResponse(UniversalBaseModel):
    """
    Closed public result for a recorded MLflow assessment.
    """

    trace_id: str
    name: typing.Optional[TraceFeedbackResponseName] = None
    value: bool
    assessment_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
