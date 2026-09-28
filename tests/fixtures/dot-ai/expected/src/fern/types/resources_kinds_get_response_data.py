

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_kinds_get_response_data_kinds_item import ResourcesKindsGetResponseDataKindsItem


class ResourcesKindsGetResponseData(UniversalBaseModel):
    kinds: typing.List[ResourcesKindsGetResponseDataKindsItem] = pydantic.Field()
    """
    List of resource kinds with counts
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
