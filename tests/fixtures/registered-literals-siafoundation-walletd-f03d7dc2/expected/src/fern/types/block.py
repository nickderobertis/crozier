

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .block_id import BlockId
from .consensus_transaction import ConsensusTransaction
from .consensus_v2block_data import ConsensusV2BlockData
from .siacoin_output import SiacoinOutput


class Block(UniversalBaseModel):
    """
    Block as returned by the walletd consensus endpoints with origin information for inputs.
    """

    id: BlockId
    parent_id: typing_extensions.Annotated[BlockId, FieldMetadata(alias="parentID"), pydantic.Field(alias="parentID")]
    nonce: int
    timestamp: dt.datetime
    miner_payouts: typing_extensions.Annotated[
        typing.List[SiacoinOutput], FieldMetadata(alias="minerPayouts"), pydantic.Field(alias="minerPayouts")
    ]
    transactions: typing.List[ConsensusTransaction]
    v2: typing.Optional[ConsensusV2BlockData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
