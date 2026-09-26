

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resource_get_response_data import ResourceGetResponseData
from .resource_get_response_meta import ResourceGetResponseMeta


class ResourceGetResponse(UniversalBaseModel):
    success: bool
    data: ResourceGetResponseData
    meta: typing.Optional[ResourceGetResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
