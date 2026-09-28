

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_get_error503error import ResourcesGetError503Error
from .resources_get_error503meta import ResourcesGetError503Meta


class ResourcesGetError503(UniversalBaseModel):
    success: bool
    error: ResourcesGetError503Error
    meta: typing.Optional[ResourcesGetError503Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
