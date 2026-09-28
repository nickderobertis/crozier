

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_search_get_response_data import ResourcesSearchGetResponseData
from .resources_search_get_response_meta import ResourcesSearchGetResponseMeta


class ResourcesSearchGetResponse(UniversalBaseModel):
    success: bool
    data: ResourcesSearchGetResponseData
    meta: typing.Optional[ResourcesSearchGetResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
