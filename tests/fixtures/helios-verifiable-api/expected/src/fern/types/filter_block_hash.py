

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .filter_block_hash_address import FilterBlockHashAddress
from .filter_topics import FilterTopics
from .hash32 import Hash32


class FilterBlockHash(UniversalBaseModel):
    block_hash: typing_extensions.Annotated[Hash32, FieldMetadata(alias="blockHash"), pydantic.Field(alias="blockHash")]
    address: typing.Optional[FilterBlockHashAddress] = None
    topics: typing.Optional[FilterTopics] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
