

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resource_get_error400error import ResourceGetError400Error
from .resource_get_error400meta import ResourceGetError400Meta


class ResourceGetError400(UniversalBaseModel):
    success: bool
    error: ResourceGetError400Error
    meta: typing.Optional[ResourceGetError400Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
