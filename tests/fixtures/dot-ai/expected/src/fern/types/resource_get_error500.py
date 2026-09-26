

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resource_get_error500error import ResourceGetError500Error
from .resource_get_error500meta import ResourceGetError500Meta


class ResourceGetError500(UniversalBaseModel):
    success: bool
    error: ResourceGetError500Error
    meta: typing.Optional[ResourceGetError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
