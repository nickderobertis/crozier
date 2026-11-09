

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .algorithm_advisory_action import AlgorithmAdvisoryAction
from .algorithm_advisory_type import AlgorithmAdvisoryType
from .composite_signature import CompositeSignature


class AlgorithmAdvisory(UniversalBaseModel):
    type: AlgorithmAdvisoryType
    advisory_id: str
    affected_algorithms: typing.List[str]
    action: AlgorithmAdvisoryAction
    severity: typing.Optional[str] = None
    effective_date: typing.Optional[dt.datetime] = None
    grace_period_days: typing.Optional[int] = None
    replacement_algorithms: typing.Optional[typing.List[str]] = None
    composite_sig: typing.Optional[CompositeSignature] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
