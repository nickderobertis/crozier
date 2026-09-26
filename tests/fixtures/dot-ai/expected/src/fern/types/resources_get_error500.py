

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_get_error500error import ResourcesGetError500Error
from .resources_get_error500meta import ResourcesGetError500Meta


class ResourcesGetError500(UniversalBaseModel):
    success: bool
    error: ResourcesGetError500Error
    meta: typing.Optional[ResourcesGetError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
