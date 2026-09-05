

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .external_unified_event import ExternalUnifiedEvent
from .paging import Paging


class CollectionResponseExternalUnifiedEvent(UniversalBaseModel):
    paging: typing.Optional[Paging] = None
    results: typing.List[ExternalUnifiedEvent] = pydantic.Field()
    """
    
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
