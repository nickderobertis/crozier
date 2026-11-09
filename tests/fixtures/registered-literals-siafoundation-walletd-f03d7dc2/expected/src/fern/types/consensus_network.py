

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .block_id import BlockId
from .consensus_network_hardfork_asic import ConsensusNetworkHardforkAsic
from .consensus_network_hardfork_dev_addr import ConsensusNetworkHardforkDevAddr
from .consensus_network_hardfork_foundation import ConsensusNetworkHardforkFoundation
from .consensus_network_hardfork_oak import ConsensusNetworkHardforkOak
from .consensus_network_hardfork_storage_proof import ConsensusNetworkHardforkStorageProof
from .consensus_network_hardfork_tax import ConsensusNetworkHardforkTax
from .consensus_network_hardfork_v2 import ConsensusNetworkHardforkV2
from .currency import Currency


class ConsensusNetwork(UniversalBaseModel):
    """
    Parameters that define network-wide consensus constants.
    """

    name: str = pydantic.Field()
    """
    Human friendly name of the network (e.g. mainnet, zen, anagami).
    """

    initial_coinbase: typing_extensions.Annotated[
        Currency, FieldMetadata(alias="initialCoinbase"), pydantic.Field(alias="initialCoinbase")
    ]
    minimum_coinbase: typing_extensions.Annotated[
        Currency, FieldMetadata(alias="minimumCoinbase"), pydantic.Field(alias="minimumCoinbase")
    ]
    initial_target: typing_extensions.Annotated[
        BlockId, FieldMetadata(alias="initialTarget"), pydantic.Field(alias="initialTarget")
    ]
    block_interval: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="blockInterval"),
        pydantic.Field(
            alias="blockInterval", description='Target block interval expressed as a Go duration string (e.g. "600s").'
        ),
    ]
    """
    Target block interval expressed as a Go duration string (e.g. "600s").
    """

    maturity_delay: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="maturityDelay"),
        pydantic.Field(alias="maturityDelay", description="Number of confirmations before miner payouts mature."),
    ]
    """
    Number of confirmations before miner payouts mature.
    """

    hardfork_dev_addr: typing_extensions.Annotated[
        ConsensusNetworkHardforkDevAddr, FieldMetadata(alias="hardforkDevAddr"), pydantic.Field(alias="hardforkDevAddr")
    ]
    hardfork_tax: typing_extensions.Annotated[
        ConsensusNetworkHardforkTax, FieldMetadata(alias="hardforkTax"), pydantic.Field(alias="hardforkTax")
    ]
    hardfork_storage_proof: typing_extensions.Annotated[
        ConsensusNetworkHardforkStorageProof,
        FieldMetadata(alias="hardforkStorageProof"),
        pydantic.Field(alias="hardforkStorageProof"),
    ]
    hardfork_oak: typing_extensions.Annotated[
        ConsensusNetworkHardforkOak, FieldMetadata(alias="hardforkOak"), pydantic.Field(alias="hardforkOak")
    ]
    hardfork_asic: typing_extensions.Annotated[
        ConsensusNetworkHardforkAsic, FieldMetadata(alias="hardforkASIC"), pydantic.Field(alias="hardforkASIC")
    ]
    hardfork_foundation: typing_extensions.Annotated[
        ConsensusNetworkHardforkFoundation,
        FieldMetadata(alias="hardforkFoundation"),
        pydantic.Field(alias="hardforkFoundation"),
    ]
    hardfork_v2: typing_extensions.Annotated[
        ConsensusNetworkHardforkV2, FieldMetadata(alias="hardforkV2"), pydantic.Field(alias="hardforkV2")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
