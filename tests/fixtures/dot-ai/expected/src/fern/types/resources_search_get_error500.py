

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_search_get_error500error import ResourcesSearchGetError500Error
from .resources_search_get_error500meta import ResourcesSearchGetError500Meta


class ResourcesSearchGetError500(UniversalBaseModel):
    success: bool
    error: ResourcesSearchGetError500Error
    meta: typing.Optional[ResourcesSearchGetError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
