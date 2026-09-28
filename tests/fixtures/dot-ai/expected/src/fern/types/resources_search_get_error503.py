

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_search_get_error503error import ResourcesSearchGetError503Error
from .resources_search_get_error503meta import ResourcesSearchGetError503Meta


class ResourcesSearchGetError503(UniversalBaseModel):
    success: bool
    error: ResourcesSearchGetError503Error
    meta: typing.Optional[ResourcesSearchGetError503Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
