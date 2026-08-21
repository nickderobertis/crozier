

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .filter_from_block_address import FilterFromBlockAddress
from .filter_topics import FilterTopics


class FilterFromBlock(UniversalBaseModel):
    from_block: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="fromBlock"), pydantic.Field(alias="fromBlock")
    ] = None
    to_block: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="toBlock"), pydantic.Field(alias="toBlock")
    ] = None
    address: typing.Optional[FilterFromBlockAddress] = None
    topics: typing.Optional[FilterTopics] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
