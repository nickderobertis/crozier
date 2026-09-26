

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_sync_post_error400error import ResourcesSyncPostError400Error
from .resources_sync_post_error400meta import ResourcesSyncPostError400Meta


class ResourcesSyncPostError400(UniversalBaseModel):
    success: bool
    error: ResourcesSyncPostError400Error
    meta: typing.Optional[ResourcesSyncPostError400Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
