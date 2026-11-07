

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .block_id import BlockId


class ConsensusNetworkHardforkAsic(UniversalBaseModel):
    height: int
    oak_time: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="oakTime"),
        pydantic.Field(alias="oakTime", description="Duration encoded as a Go duration string."),
    ]
    """
    Duration encoded as a Go duration string.
    """

    oak_target: typing_extensions.Annotated[
        BlockId, FieldMetadata(alias="oakTarget"), pydantic.Field(alias="oakTarget")
    ]
    nonce_factor: typing_extensions.Annotated[
        int, FieldMetadata(alias="nonceFactor"), pydantic.Field(alias="nonceFactor")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
