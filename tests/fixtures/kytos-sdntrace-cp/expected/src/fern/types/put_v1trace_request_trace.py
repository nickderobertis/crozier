

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .put_v1trace_request_trace_eth import PutV1TraceRequestTraceEth
from .put_v1trace_request_trace_ip import PutV1TraceRequestTraceIp
from .put_v1trace_request_trace_switch import PutV1TraceRequestTraceSwitch
from .put_v1trace_request_trace_tp import PutV1TraceRequestTraceTp


class PutV1TraceRequestTrace(UniversalBaseModel):
    switch: PutV1TraceRequestTraceSwitch
    eth: typing.Optional[PutV1TraceRequestTraceEth] = None
    ip: typing.Optional[PutV1TraceRequestTraceIp] = None
    tp: typing.Optional[PutV1TraceRequestTraceTp] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
