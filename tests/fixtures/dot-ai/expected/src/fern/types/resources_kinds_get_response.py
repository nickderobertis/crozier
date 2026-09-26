

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_kinds_get_response_data import ResourcesKindsGetResponseData
from .resources_kinds_get_response_meta import ResourcesKindsGetResponseMeta


class ResourcesKindsGetResponse(UniversalBaseModel):
    success: bool
    data: ResourcesKindsGetResponseData
    meta: typing.Optional[ResourcesKindsGetResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
