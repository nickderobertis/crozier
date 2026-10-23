

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetChainsChainIdAssetsSymbolPoolsResponseDiscoveryItem(UniversalBaseModel):
    venue: str
    scanned: bool = pydantic.Field()
    """
    Discovery has read this venue at least once; false means no pool from it is listed yet because nothing has looked.
    """

    scanned_to_block: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="scannedToBlock"), pydantic.Field(alias="scannedToBlock")
    ] = None
    head_block: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="headBlock"), pydantic.Field(alias="headBlock")
    ] = None
    head_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="headAt"),
        pydantic.Field(alias="headAt", description="When the chain head above was read."),
    ] = None
    """
    When the chain head above was read.
    """

    blocks_behind: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="blocksBehind"), pydantic.Field(alias="blocksBehind")
    ] = None
    reading_history: typing_extensions.Annotated[
        bool, FieldMetadata(alias="readingHistory"), pydantic.Field(alias="readingHistory")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
