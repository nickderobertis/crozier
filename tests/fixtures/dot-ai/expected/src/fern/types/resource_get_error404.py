

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resource_get_error404error import ResourceGetError404Error
from .resource_get_error404meta import ResourceGetError404Meta


class ResourceGetError404(UniversalBaseModel):
    success: bool
    error: ResourceGetError404Error
    meta: typing.Optional[ResourceGetError404Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
