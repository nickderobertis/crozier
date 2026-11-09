

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .block_id import BlockId
from .chain_index import ChainIndex
from .currency import Currency
from .element_accumulator import ElementAccumulator
from .work import Work


class ConsensusState(UniversalBaseModel):
    """
    Snapshot of consensus-related chain state at a specific tip.
    """

    index: ChainIndex
    prev_timestamps: typing_extensions.Annotated[
        typing.List[dt.datetime],
        FieldMetadata(alias="prevTimestamps"),
        pydantic.Field(alias="prevTimestamps", description="Last 11 block timestamps, newest first."),
    ]
    """
    Last 11 block timestamps, newest first.
    """

    depth: BlockId
    child_target: typing_extensions.Annotated[
        BlockId, FieldMetadata(alias="childTarget"), pydantic.Field(alias="childTarget")
    ]
    siafund_tax_revenue: typing_extensions.Annotated[
        Currency, FieldMetadata(alias="siafundTaxRevenue"), pydantic.Field(alias="siafundTaxRevenue")
    ]
    oak_time: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="oakTime"),
        pydantic.Field(alias="oakTime", description="Weighted average block time encoded as a Go duration string."),
    ]
    """
    Weighted average block time encoded as a Go duration string.
    """

    oak_target: typing_extensions.Annotated[
        BlockId, FieldMetadata(alias="oakTarget"), pydantic.Field(alias="oakTarget")
    ]
    foundation_subsidy_address: typing_extensions.Annotated[
        Address, FieldMetadata(alias="foundationSubsidyAddress"), pydantic.Field(alias="foundationSubsidyAddress")
    ]
    foundation_management_address: typing_extensions.Annotated[
        Address, FieldMetadata(alias="foundationManagementAddress"), pydantic.Field(alias="foundationManagementAddress")
    ]
    total_work: typing_extensions.Annotated[Work, FieldMetadata(alias="totalWork"), pydantic.Field(alias="totalWork")]
    difficulty: Work
    oak_work: typing_extensions.Annotated[Work, FieldMetadata(alias="oakWork"), pydantic.Field(alias="oakWork")]
    elements: ElementAccumulator
    attestations: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
