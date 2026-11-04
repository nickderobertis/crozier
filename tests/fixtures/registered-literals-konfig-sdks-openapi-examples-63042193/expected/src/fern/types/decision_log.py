

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .decision import Decision
from .decision_log_metadata import DecisionLogMetadata


class DecisionLog(UniversalBaseModel):
    created_at: typing.Optional[dt.datetime] = None
    decision: typing.Optional[Decision] = None
    id: typing.Optional[str] = None
    metadata: typing.Optional[DecisionLogMetadata] = None
    policies: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    policy-name-to-hash-map
    """

    time_taken_ms: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
