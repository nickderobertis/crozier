

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ConsensusNetworkHardforkOak(UniversalBaseModel):
    height: int
    fix_height: typing_extensions.Annotated[int, FieldMetadata(alias="fixHeight"), pydantic.Field(alias="fixHeight")]
    genesis_timestamp: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="genesisTimestamp"), pydantic.Field(alias="genesisTimestamp")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
