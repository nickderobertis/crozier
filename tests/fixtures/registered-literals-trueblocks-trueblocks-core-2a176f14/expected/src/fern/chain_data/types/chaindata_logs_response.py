

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .chaindata_logs_response_data_item import ChaindataLogsResponseDataItem


class ChaindataLogsResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[ChaindataLogsResponseDataItem]] = pydantic.Field(default=None)
    """
    Produces <a href="/data-model/other/#function">Function</a>, <a href="/data-model/chaindata/#log">Log</a>, <a href="/data-model/other/#message">Message</a> or <a href="/data-model/other/#parameter">Parameter</a> data. Corresponds to the <a href="/chifra/chaindata/#chifra-logs">chifra logs</a> command line.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ChaindataLogsResponse)
