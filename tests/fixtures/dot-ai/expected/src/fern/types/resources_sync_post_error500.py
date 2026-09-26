

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_sync_post_error500error import ResourcesSyncPostError500Error
from .resources_sync_post_error500meta import ResourcesSyncPostError500Meta


class ResourcesSyncPostError500(UniversalBaseModel):
    success: bool
    error: ResourcesSyncPostError500Error
    meta: typing.Optional[ResourcesSyncPostError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
