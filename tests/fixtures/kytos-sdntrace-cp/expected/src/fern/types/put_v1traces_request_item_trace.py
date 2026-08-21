

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .put_v1traces_request_item_trace_eth import PutV1TracesRequestItemTraceEth
from .put_v1traces_request_item_trace_ip import PutV1TracesRequestItemTraceIp
from .put_v1traces_request_item_trace_switch import PutV1TracesRequestItemTraceSwitch
from .put_v1traces_request_item_trace_tp import PutV1TracesRequestItemTraceTp


class PutV1TracesRequestItemTrace(UniversalBaseModel):
    switch: PutV1TracesRequestItemTraceSwitch
    eth: typing.Optional[PutV1TracesRequestItemTraceEth] = None
    ip: typing.Optional[PutV1TracesRequestItemTraceIp] = None
    tp: typing.Optional[PutV1TracesRequestItemTraceTp] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
