

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_collaboration_resources_search_collections200response_ocs import (
    CoreCollaborationResourcesSearchCollections200ResponseOcs,
)


class CoreCollaborationResourcesSearchCollections200Response(UniversalBaseModel):
    ocs: CoreCollaborationResourcesSearchCollections200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
