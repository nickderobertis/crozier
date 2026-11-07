

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .admin_chunks_response_data_item import AdminChunksResponseDataItem


class AdminChunksResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[AdminChunksResponseDataItem]] = pydantic.Field(default=None)
    """
    Produces <a href="/data-model/accounts/#appearance">Appearance</a>, <a href="/data-model/accounts/#appearancetable">AppearanceTable</a>, <a href="/data-model/admin/#chunkaddress">ChunkAddress</a>, <a href="/data-model/admin/#chunkbloom">ChunkBloom</a>, <a href="/data-model/admin/#chunkindex">ChunkIndex</a>, <a href="/data-model/admin/#chunkpin">ChunkPin</a>, <a href="/data-model/admin/#chunkrecord">ChunkRecord</a>, <a href="/data-model/admin/#chunkstats">ChunkStats</a>, <a href="/data-model/other/#count">Count</a>, <a href="/data-model/admin/#ipfspin">IpfsPin</a>, <a href="/data-model/admin/#manifest">Manifest</a>, <a href="/data-model/other/#message">Message</a>, <a href="/data-model/admin/#rangedates">RangeDates</a> or <a href="/data-model/admin/#reportcheck">ReportCheck</a> data. Corresponds to the <a href="/chifra/admin/#chifra-chunks">chifra chunks</a> command line.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
