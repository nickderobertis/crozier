

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .chaindata_receipts_response_data_item import ChaindataReceiptsResponseDataItem


class ChaindataReceiptsResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[ChaindataReceiptsResponseDataItem]] = pydantic.Field(default=None)
    """
    Produces <a href="/data-model/other/#function">Function</a>, <a href="/data-model/other/#parameter">Parameter</a> or <a href="/data-model/chaindata/#receipt">Receipt</a> data. Corresponds to the <a href="/chifra/chaindata/#chifra-receipts">chifra receipts</a> command line.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ChaindataReceiptsResponse)
