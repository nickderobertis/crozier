

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .signal_evaluate_core_attributes import SignalEvaluateCoreAttributes
from .signal_scores import SignalScores
from .signal_warning import SignalWarning


class SignalEvaluateResponse(UniversalBaseModel):
    """
    SignalEvaluateResponse defines the response schema for `/signal/income/evaluate`
    """

    core_attributes: typing.Optional[SignalEvaluateCoreAttributes] = None
    request_id: RequestId
    scores: SignalScores
    warnings: typing.Optional[typing.List[SignalWarning]] = pydantic.Field(default=None)
    """
    If bank information was not able to be used as features into the Signal model, this array contains warnings describing why we were missing bank data
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
