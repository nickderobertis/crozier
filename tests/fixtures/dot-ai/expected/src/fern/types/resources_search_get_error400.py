

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_search_get_error400error import ResourcesSearchGetError400Error
from .resources_search_get_error400meta import ResourcesSearchGetError400Meta


class ResourcesSearchGetError400(UniversalBaseModel):
    success: bool
    error: ResourcesSearchGetError400Error
    meta: typing.Optional[ResourcesSearchGetError400Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
