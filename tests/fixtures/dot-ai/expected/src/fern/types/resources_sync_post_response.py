

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_sync_post_response_data import ResourcesSyncPostResponseData
from .resources_sync_post_response_meta import ResourcesSyncPostResponseMeta


class ResourcesSyncPostResponse(UniversalBaseModel):
    success: bool
    data: ResourcesSyncPostResponseData
    meta: typing.Optional[ResourcesSyncPostResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
