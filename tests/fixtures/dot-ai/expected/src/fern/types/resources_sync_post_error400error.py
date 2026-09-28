

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_sync_post_error400error_code import ResourcesSyncPostError400ErrorCode


class ResourcesSyncPostError400Error(UniversalBaseModel):
    code: ResourcesSyncPostError400ErrorCode
    message: str
    details: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
