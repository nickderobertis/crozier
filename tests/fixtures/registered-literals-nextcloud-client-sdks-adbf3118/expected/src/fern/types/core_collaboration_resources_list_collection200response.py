

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_collaboration_resources_list_collection200response_ocs import (
    CoreCollaborationResourcesListCollection200ResponseOcs,
)


class CoreCollaborationResourcesListCollection200Response(UniversalBaseModel):
    ocs: CoreCollaborationResourcesListCollection200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
