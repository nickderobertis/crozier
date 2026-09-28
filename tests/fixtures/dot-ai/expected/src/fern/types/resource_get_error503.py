

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resource_get_error503error import ResourceGetError503Error
from .resource_get_error503meta import ResourceGetError503Meta


class ResourceGetError503(UniversalBaseModel):
    success: bool
    error: ResourceGetError503Error
    meta: typing.Optional[ResourceGetError503Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
