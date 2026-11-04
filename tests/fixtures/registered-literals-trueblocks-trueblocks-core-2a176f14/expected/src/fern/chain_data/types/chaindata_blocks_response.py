

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chaindata_blocks_response_data_item import ChaindataBlocksResponseDataItem


class ChaindataBlocksResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[ChaindataBlocksResponseDataItem]] = pydantic.Field(default=None)
    """
    Produces <a href="/data-model/accounts/#appearance">Appearance</a>, <a href="/data-model/chaindata/#block">Block</a>, <a href="/data-model/chaindata/#blockcount">BlockCount</a>, <a href="/data-model/chaindata/#lightblock">LightBlock</a>, <a href="/data-model/chaindata/#log">Log</a>, <a href="/data-model/other/#message">Message</a>, <a href="/data-model/chaindata/#trace">Trace</a>, <a href="/data-model/chaindata/#traceaction">TraceAction</a>, <a href="/data-model/chaindata/#traceresult">TraceResult</a> or <a href="/data-model/chaindata/#withdrawal">Withdrawal</a> data. Corresponds to the <a href="/chifra/chaindata/#chifra-blocks">chifra blocks</a> command line.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
