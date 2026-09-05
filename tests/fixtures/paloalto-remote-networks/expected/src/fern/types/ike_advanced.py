

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ike_advanced_fragmentation import IkeAdvancedFragmentation
from .ike_advanced_nat_traversal import IkeAdvancedNatTraversal


class IkeAdvanced(UniversalBaseModel):
    fragmentation: typing.Optional[IkeAdvancedFragmentation] = None
    nat_traversal: typing.Optional[IkeAdvancedNatTraversal] = None
    passive_mode: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
