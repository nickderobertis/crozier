

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_kinds_get_error500error import ResourcesKindsGetError500Error
from .resources_kinds_get_error500meta import ResourcesKindsGetError500Meta


class ResourcesKindsGetError500(UniversalBaseModel):
    success: bool
    error: ResourcesKindsGetError500Error
    meta: typing.Optional[ResourcesKindsGetError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
