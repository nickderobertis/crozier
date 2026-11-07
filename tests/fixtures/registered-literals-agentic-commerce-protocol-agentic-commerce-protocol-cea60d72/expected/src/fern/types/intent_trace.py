

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .intent_trace_metadata_value import IntentTraceMetadataValue
from .intent_trace_reason_code import IntentTraceReasonCode


class IntentTrace(UniversalBaseModel):
    reason_code: IntentTraceReasonCode = pydantic.Field()
    """
    Reason for abandonment. This enum is extensible: servers SHOULD accept
    unrecognized values and treat them as "other" (see RFC Section 7.2).
    Validators SHOULD be configured for lenient enum handling.
    """

    trace_summary: typing.Optional[str] = pydantic.Field(default=None)
    """
    A generated summary of the specific objection or negotiation gap.
    """

    metadata: typing.Optional[typing.Dict[str, IntentTraceMetadataValue]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
