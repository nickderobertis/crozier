

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_collection import CoreCollection
from .ocs_meta import OcsMeta


class CoreCollaborationResourcesSearchCollections200ResponseOcs(UniversalBaseModel):
    meta: OcsMeta
    data: typing.List[CoreCollection]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
