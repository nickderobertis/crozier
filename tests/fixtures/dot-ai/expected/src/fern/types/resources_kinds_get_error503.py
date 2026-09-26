

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_kinds_get_error503error import ResourcesKindsGetError503Error
from .resources_kinds_get_error503meta import ResourcesKindsGetError503Meta


class ResourcesKindsGetError503(UniversalBaseModel):
    success: bool
    error: ResourcesKindsGetError503Error
    meta: typing.Optional[ResourcesKindsGetError503Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
