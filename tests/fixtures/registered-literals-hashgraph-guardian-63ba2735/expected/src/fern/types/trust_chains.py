

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .trust_chains_chain_item import TrustChainsChainItem
from .trust_chains_user_map_item import TrustChainsUserMapItem


class TrustChains(UniversalBaseModel):
    chain: typing.List[TrustChainsChainItem]
    user_map: typing_extensions.Annotated[
        typing.List[TrustChainsUserMapItem], FieldMetadata(alias="userMap"), pydantic.Field(alias="userMap")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
