

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_get_error400error import ResourcesGetError400Error
from .resources_get_error400meta import ResourcesGetError400Meta


class ResourcesGetError400(UniversalBaseModel):
    success: bool
    error: ResourcesGetError400Error
    meta: typing.Optional[ResourcesGetError400Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
