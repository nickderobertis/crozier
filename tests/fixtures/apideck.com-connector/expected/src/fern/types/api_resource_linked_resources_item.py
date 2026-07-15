

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resource_id import ResourceId
from .unified_property import UnifiedProperty


class ApiResourceLinkedResourcesItem(UniversalBaseModel):
    id: typing.Optional[ResourceId] = None
    unified_property: typing.Optional[UnifiedProperty] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
