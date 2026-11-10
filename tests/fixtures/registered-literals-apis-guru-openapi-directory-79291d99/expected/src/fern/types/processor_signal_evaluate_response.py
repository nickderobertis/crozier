

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .signal_evaluate_core_attributes import SignalEvaluateCoreAttributes
from .signal_scores import SignalScores


class ProcessorSignalEvaluateResponse(UniversalBaseModel):
    """
    ProcessorSignalEvaluateResponse defines the response schema for `/processor/signal/evaluate`
    """

    core_attributes: typing.Optional[SignalEvaluateCoreAttributes] = None
    request_id: RequestId
    scores: SignalScores

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
