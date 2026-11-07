

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .chainstate_state_response_data_item import ChainstateStateResponseDataItem


class ChainstateStateResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[ChainstateStateResponseDataItem]] = pydantic.Field(default=None)
    """
    Produces <a href="/data-model/other/#function">Function</a>, <a href="/data-model/other/#message">Message</a>, <a href="/data-model/other/#parameter">Parameter</a>, <a href="/data-model/chainstate/#result">Result</a> or <a href="/data-model/chainstate/#state">State</a> data. Corresponds to the <a href="/chifra/chainstate/#chifra-state">chifra state</a> command line.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ChainstateStateResponse)
