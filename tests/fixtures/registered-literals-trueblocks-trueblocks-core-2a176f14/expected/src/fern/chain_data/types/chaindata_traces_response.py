

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .chaindata_traces_response_data_item import ChaindataTracesResponseDataItem


class ChaindataTracesResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[ChaindataTracesResponseDataItem]] = pydantic.Field(default=None)
    """
    Produces <a href="/data-model/other/#function">Function</a>, <a href="/data-model/other/#message">Message</a>, <a href="/data-model/other/#parameter">Parameter</a>, <a href="/data-model/chaindata/#trace">Trace</a>, <a href="/data-model/chaindata/#traceaction">TraceAction</a>, <a href="/data-model/chaindata/#tracecount">TraceCount</a>, <a href="/data-model/chaindata/#tracefilter">TraceFilter</a> or <a href="/data-model/chaindata/#traceresult">TraceResult</a> data. Corresponds to the <a href="/chifra/chaindata/#chifra-traces">chifra traces</a> command line.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ChaindataTracesResponse)
