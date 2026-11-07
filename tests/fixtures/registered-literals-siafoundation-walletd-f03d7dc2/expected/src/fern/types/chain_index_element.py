

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .block_id import BlockId
from .chain_index import ChainIndex
from .state_element import StateElement


class ChainIndexElement(UniversalBaseModel):
    id: BlockId
    state_element: typing_extensions.Annotated[
        StateElement, FieldMetadata(alias="stateElement"), pydantic.Field(alias="stateElement")
    ]
    chain_index: typing_extensions.Annotated[
        ChainIndex, FieldMetadata(alias="chainIndex"), pydantic.Field(alias="chainIndex")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
